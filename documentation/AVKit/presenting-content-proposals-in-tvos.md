# Presenting Content Proposals in tvOS

**Framework**: AVKit

Display a preview of an upcoming media item at the conclusion of the currently playing media item.

#### Overview

Media apps presenting serialized content, such as a TV show, often display a preview of the next episode in the series when you finish watching the current one. The user interface for this preview usually contains artwork and information about the proposed content. It also includes options for the user to either watch the next episode or return to the main menu. You add this functionality to your app using AVKit’s content proposals.

##### Create a Content Proposal

You create a content proposal using the [`AVContentProposal`](avcontentproposal.md) class. This type models the data about the proposed content, such as its title, preview image, metadata, and content URL, and the time at which to present the proposal. You create and configure a content proposal instance as shown in the following code:

```swift
func makeProposal() -> AVContentProposal {

    // Present 10 seconds prior to the end of current presentation
    let time = currentAsset.duration - CMTime(value: 10, timescale: 1)
    let title = "My Show: Episode 2"
    let image = UIImage(named: "ms_ep2")!
    let proposal = AVContentProposal(contentTimeForTransition: time, title: title, previewImage: image)

    // Set custom metadata
    proposal.metadata = [
        makeMetadataItem(.commonIdentifierDescription, value: "Episode 2 Description"),
        makeMetadataItem(.iTunesMetadataContentRating, value: "TV-14"),
        makeMetadataItem(.quickTimeMetadataGenre, value: "Comedy")
    ]

    // Set content URL
    proposal.url = // The upcoming asset's URL
    
    // Return the created proposal.
    return proposal
}

private func makeMetadataItem(_ identifier: AVMetadataIdentifier, value: Any) -> AVMetadataItem {
    let item = AVMutableMetadataItem()
    item.identifier = identifier
    item.value = value as? NSCopying & NSObjectProtocol
    item.extendedLanguageTag = "und"
    return item.copy() as! AVMetadataItem
}
```

##### Create the Content Proposals User Interface

In addition to defining your content proposal’s data, you also need to create an interface to present this data to the user. You create this interface by subclassing the AVKit framework’s [`AVContentProposalViewController`](avcontentproposalviewcontroller.md) class. At runtime, the system passes your subclass a reference to the current [`AVContentProposal`](avcontentproposal.md), providing you the data to present. Your user interface should provide visual and descriptive information about the proposed content, and should also include options for the user to accept or reject the proposal.

When the system presents your proposal, it displays it over the currently playing full-screen video. You may want to scale this video to a smaller size so you can make more room to display the details of the proposed content. To do this, you override the view controller’s [`preferredPlayerViewFrame`](avcontentproposalviewcontroller/preferredplayerviewframe.md) property and return the desired video frame.

```swift
override var preferredPlayerViewFrame: CGRect {
    guard let frame = playerViewController?.view.frame else { return CGRect.zero }
    // Present the current video in a 960x540 window centered at the top of the window
    return CGRect(x: frame.midX / 2.0, y: 0, width: 960, height: 540)
}
```

When the system presents the proposal, the player’s view automatically animates to the specified frame.

> **Note**:  To lay out your content relative to the newly sized and positioned video frame, you use the [`UILayoutGuide`](https://developer.apple.com/documentation/UIKit/UILayoutGuide) provided by the view controller’s [`playerLayoutGuide`](avcontentproposalviewcontroller/playerlayoutguide.md) property.

 To lay out your content relative to the newly sized and positioned video frame, you use the [`UILayoutGuide`](https://developer.apple.com/documentation/UIKit/UILayoutGuide) provided by the view controller’s [`playerLayoutGuide`](avcontentproposalviewcontroller/playerlayoutguide.md) property.

##### Add Controls to the Content Proposal

Your presented user interface should also provide controls so the user can accept or reject the proposal. The event handlers for these actions should call the controller’s [`dismissContentProposal(for:animated:completion:)`](avcontentproposalviewcontroller/dismisscontentproposal(for:animated:completion:).md) method, indicating the user’s choice.

```swift
// Handle acceptance
@IBAction func acceptContentProposal(_ sender: AnyObject) {
    dismissContentProposal(for: .accept, animated: true)
}

// Handle rejection
@IBAction func rejectContentProposal(_ sender: AnyObject){
    dismissContentProposal(for: .reject, animated: true)
}
```

##### Make the Content Proposal Eligible to Be Presented

To make your content proposal eligible for the system to present, set it as the [`nextContentProposal`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/nextContentProposal) property value of the current [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem). The following example shows how to configure this property value in a playback app that manages a queue of `Video` objects, which is a custom value type that models the data of an individual video in the queue. The example code creates the required playback objects, creates a new [`AVContentProposal`](avcontentproposal.md) for the next video in the queue, and sets the video as the player item’s [`nextContentProposal`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/nextContentProposal).

```swift
func prepareToPlay() {
    // Associate the AVPlayer with the AVPlayerViewController
    playerViewController?.player = player
    playerViewController?.delegate = self

    // Create a new AVPlayerItem with the current video's URL
    let playerItem = AVPlayerItem(url: currentVideo.url)
    player.replaceCurrentItem(with: playerItem)

    // Create an AVContentProposal for the next video (if it exists)
    playerItem.nextContentProposal = makeContentProposal(for: currentVideo.nextVideo)
    player.play()
}
 
func makeContentProposal(for video: Video?) -> AVContentProposal? {
    guard let video = video else { return nil }
    guard let currentAsset = player.currentItem?.asset else { return nil } 

    // Start the proposal within presentationInterval of the asset's duration
    let time = currentAsset.duration - video.presentationInterval
    let title = video.title
    let image = video.image

    // Create a new content proposal with the time, title, and image
    let contentProposal = AVContentProposal(contentTimeForTransition: time, title: title, previewImage: image)

    // Set the content URL for the proposal
    contentProposal.url = video.url
    // Automatically accept the proposal 1 second from playback end time
    contentProposal.automaticAcceptanceInterval = -1.0
    return contentProposal
}
```

##### Present the Content Proposal

With the content proposal set as the player item’s [`nextContentProposal`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/nextContentProposal), the next step is to implement the methods of the [`AVPlayerViewControllerDelegate`](avplayerviewcontrollerdelegate.md) protocol. You use these methods to define how the system presents the content proposal, as well as to handle the acceptance or rejection of the proposed content.

To present your custom view controller in response to a request to present the next content proposal, implement the [`playerViewController(_:shouldPresent:)`](avplayerviewcontrollerdelegate/playerviewcontroller(_:shouldpresent:).md) method. In this method, you set an instance of your custom [`AVContentProposalViewController`](avcontentproposalviewcontroller.md) as the player view controller’s [`contentProposalViewController`](avplayerviewcontroller/contentproposalviewcontroller.md) property.

```swift
func playerViewController(_ playerViewController: AVPlayerViewController, shouldPresent proposal: AVContentProposal) -> Bool {
    // Set the presentation to use on the player view controller for this content proposal
    playerViewController.contentProposalViewController = NextVideoProposalViewController()
    return true
}
```

If the presented [`AVContentProposal`](avcontentproposal.md) provides a valid content URL, the player view controller can automatically handle its acceptance or rejection. However, if you need more control over the handling of these actions, implement the [`playerViewController(_:didAccept:)`](avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:).md) and [`playerViewController(_:didReject:)`](avplayerviewcontrollerdelegate/playerviewcontroller(_:didreject:).md) methods. For example, the following code implements the [`playerViewController(_:didAccept:)`](avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:).md)method to play the proposed video and create a new content proposal for the next video in the queue.

```swift
func playerViewController(_ playerViewController: AVPlayerViewController, didAccept proposal: AVContentProposal) {
    guard let player = playerViewController.player, let url = proposal.url else { return }
    guard let video = currentVideo.nextVideo else { return }
    currentVideo = video

    // Create a new player item using the content proposal's URL
    let playerItem = AVPlayerItem(url: url)
    player.replaceCurrentItem(with: playerItem)
    player.play()

    // Prepare the new player item's next content proposal (if it exists)
    playerItem.nextContentProposal = makeContentProposal(for: currentVideo.nextVideo)
}
```

## See Also

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Working with Overlays and Parental Controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVInterstitialTimeRange](avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [class AVNavigationMarkersGroup](avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.
- [class AVDisplayManager](avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/presenting-content-proposals-in-tvos)*