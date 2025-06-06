# Adopting the system player interface in visionOS

**Framework**: Avkit

Provide an optimized viewing experience for watching 3D video content.

#### Overview

The recommended way to provide a video playback interface for your visionOS app is to adopt [`AVPlayerViewController`](avplayerviewcontroller.md). Using this class makes it simple to provide the same playback user interface and features found in system apps like TV and Music. It also provides essential system integration to deliver an optimal viewing experience whether you’re playing standard 2D content or immersive 3D video with spatial audio. This article describes best practices for presenting the player in visionOS and covers the options the player provides to customize its user interface to best fit your app.

> **Note**:  In addition to providing the system playback interface, you can also use [`AVPlayerViewController`](avplayerviewcontroller.md) to present a media-trimming experience similar to QuickTime Player in macOS. See [`Trimming and exporting media in visionOS`](trimming-and-exporting-media-in-visionos.md) for more information.

##### Explore Presentation Options

Use [`AVPlayerViewController`](avplayerviewcontroller.md) to play video in windowed environments in visionOS. It automatically adapts its user interface to best fit its presentation. For example, when you present it nested inside another view, it displays an inline user interface:

![A screenshot of a player view controller’s interface when you present it inline. In the center of the image is a button to toggle playback. On the button’s leading side, is a button to skip backwards 10 seconds, and on its trailing side, is a button to skip forward 10 seconds. Along the bottom of the image is a progress indicator that you can pinch and drag to scrub through the video presentation. At the top of the image, along the leading edge, is a button that you can tap to expand the player to fullscreen. On the top’s trailing edge is a horizontal slider to adjust the audio volume. Closer to the trailing edge is a button with an ellipsis icon that you can tap to display additional player controls.](https://docs-assets.developer.apple.com/published/2d9d5a2ff59fd104ea49079aaa9bad59/media-4266435%402x.png)

> **Note**:  When you present the player inline, it only displays standard 2D video. To play 3D content, present it fullscreen.

Present the player in full-screen mode by setting it as the exclusive root view of your app, or by presenting it using the [`fullScreenCover(item:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/fullScreenCover(item:onDismiss:content:)) modifier. In full-screen mode, the player presents a more content-forward design that dims the environment by default to provide more suitable viewing. This provides a streamlined viewing experience for both 2D and 3D content.

![A screenshot of a player view controller’s interface when you present it fullscreen. At the top, along the leading edge, is a back button to close the player, and along the trailing edge is a horizontal slider to control the audio volume. Centered along the bottom edge is a bar that contains user interface to control playback. On the leading edge of this bar are controls to toggle the state of playback and skip through the presentation. In the center is a horizontal progress slider that you can pinch to scrub through the presentation. On the trailing edge is a button with an ellipsis icon that you can tap to display additional player controls.](https://docs-assets.developer.apple.com/published/9f0ef10ff10c425bdb46888dafe56445/media-4266546%402x.png)

##### Display Supporting Metadata

The user interface displays a title view above the transport bar when the current player item contains title and subtitle metadata. When playing live-streaming content, the title view may also display a badge to indicate the content state to the viewer.

![A screenshot of the fullscreen player interface when the media contains embedded metadata. The interface displays two strings towards the bottom of its leading edge that represent the title and subtitle. The title is shown prominently in a large, bold font. Above it, the subtitle displayed in a smaller, secondary font.](https://docs-assets.developer.apple.com/published/09ea9f3982c85f7806b7f6d86630a523/media-4266545%402x.png)

The title view displays the values of an asset’s [`commonIdentifierTitle`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/commonIdentifierTitle) and [`iTunesMetadataTrackSubTitle`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/iTunesMetadataTrackSubTitle) metadata items, when available. If your media doesn’t provide embedded metadata, you can add supplemental metadata to display by creating instances of [`AVMetadataItem`](https://developer.apple.com/documentation/AVFoundation/AVMetadataItem). The table below lists the metadata values the player user interface supports.

| Metadata | Identifier | Type |
| --- | --- | --- |
| Title | [`commonIdentifierTitle`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/commonIdentifierTitle) | String |
| Subtitle | [`iTunesMetadataTrackSubTitle`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/iTunesMetadataTrackSubTitle) | String |
| Artwork | [`commonIdentifierArtwork`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/commonIdentifierArtwork) | Data |
| Description | [`commonIdentifierDescription`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/commonIdentifierDescription) | String |
| Genre | [`quickTimeMetadataGenre`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/quickTimeMetadataGenre) | String |
| Content rating | [`iTunesMetadataContentRating`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/iTunesMetadataContentRating) | String |

In an app that defines a simple structure to hold string and data items, you can map its values to their appropriate metadata identifiers and build an array of metadata items:

```swift
private func createMetadataItems(for metadata: Metadata) -> [AVMetadataItem] {
    [
        metadataItem(key: .commonIdentifierTitle, value: metadata.title),
        metadataItem(key: .iTunesMetadataTrackSubTitle, value: metadata.subtitle),
        metadataItem(key: .commonIdentifierArtwork, value: metadata.imageData),
        metadataItem(key: .commonIdentifierDescription, value: metadata.description),
        metadataItem(key: .iTunesMetadataContentRating, value: metadata.rating),
        metadataItem(key: .quickTimeMetadataGenre, value: metadata.genre)
    ]
}

private func metadataItem(key identifier: AVMetadataIdentifier,
                          value: Any) -> AVMetadataItem {
    let item = AVMutableMetadataItem()
    item.identifier = identifier
    item.value = value as? NSCopying & NSObjectProtocol
    item.extendedLanguageTag = "und"
    // Return an immutable copy of the item.
    return item.copy() as! AVMetadataItem
}
```

To apply the metadata to the current player item, set the array of metadata items as the value of the player item’s [`externalMetadata`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/externalMetadata) property:

```swift
let metadata: Metadata = // A structure that contains simple string values.
playerItem.externalMetadata = createMetadataItems(for: metadata)
```

Only the title and subtitle values display in the title view. The player presents the other supported metadata values in its Info tab, which the section below describes.

##### Display Custom Informational Views

The visionOS player UI can display one or more content tabs in the user interface to show supporting information or related content. By default, the player presents an Info tab when an asset contains embedded metadata or when you set external metadata on the player item, as the Display supporting metadata section above describes.

Your app can also present custom tabs to show supporting content. You define your tab content as standard SwiftUI views, wrap them in a [`UIHostingController`](https://developer.apple.com/documentation/SwiftUI/UIHostingController), and set them as the [`customInfoViewControllers`](avplayerviewcontroller/custominfoviewcontrollers.md) property. The player UI uses the [`title`](https://developer.apple.com/documentation/UIKit/UIViewController/title) property of the hosting controller to display as the tab title in the interface, so set this value before setting it on the player view controller.

```swift
let view = UpNextView(videos: upNextVideos)
let hostingController = UIHostingController(rootView: view)

// Set custom content tabs on the player UI.
hostingController.title = String(localized: "Up Next")

hostingController.preferredContentSize = CGSize(width: 300, height: 100)
controller.customInfoViewControllers = [hostingController]
```

![A screenshot of the fullscreen player’s displaying a custom horizontal list from a custom info view controller. The player displays a panel along its bottom edge. At the top of the panel is a close button, anchored to the leading edge, and a title that’s centered. Below these items, the custom info view controller displays a horizontally scrollable list of video cards that you can select to watch another video.](https://docs-assets.developer.apple.com/published/e931ad39e497649ad78d424fcfc7206e/media-4266544%402x.png)

##### Present Actions in the Info Tab

The player UI presents an Info tab when the asset it displays provides embedded or external metadata. The tab’s view displays the metadata details, and it may show up to two [`UIAction`](https://developer.apple.com/documentation/UIKit/UIAction) controls along its trailing edge:

![A screenshot of the fullscreen player displaying its Info tab. At the top of the Info tab is a close button, anchored to the leading edge, and the word “Info” centered along the top. Below that, on the leading edge displays metadata for the video including title, description, and content rating. Along the trailing edge of this panel are two buttons arranged vertically. The top button displays a play button and the string From Beginning that you tap to play the video from the beginning. The button is a custom action that shows an information icon - a letter I with a circle around it - and the string More Information. The action that occurs when you tap this button is up to the app.](https://docs-assets.developer.apple.com/published/be2d96b843edbfe75cf06ef3f7f658ad/media-4266547%402x.png)

Customize the actions the view presents by setting a value for the player view controller’s [`infoViewActions`](avplayerviewcontroller/infoviewactions.md) property. When playing nonlive content, this property contains a single-element array that presents an action to play the content from the beginning. You can replace the default value (if present), add an additional action, or set this property value to an empty array to display no actions. The example below shows how to add a Add to Favorites action to the view:

```swift
let infoCircle = UIImage(systemName: "info.circle")
let showMoreInfo = UIAction(title: "More Information", image: infoCircle) { action in
    // Navigate to a screen to display more information.
}
// Append the action to the array.
playerViewController.infoViewActions.append(showMoreInfo)
```

##### Display Actions Contextually

You can use the visionOS player UI to present controls contextually, which your app displays for a specific range of time in the content and then dismiss. A common use for this type of control is a skip button that displays during the title sequence of a movie or TV show. People can tap the button to bypass the introduction and quickly skip to the main content.

![A screenshot of the fullscreen player interface, with its standard controls presented. Along the bottom of the player interface’s trailing edge is a custom contextual action that displays a button with the title Skip Into. Tapping this button seeks the player forward to where the main video content begins.](https://docs-assets.developer.apple.com/published/e5661cabd2a7e401dbee035b7594de49/media-4266548%402x.png)

[`AVPlayerViewController`](avplayerviewcontroller.md) provides a [`contextualActions`](avplayerviewcontroller/contextualactions.md) property you can use to specify one or more actions to present. The player displays them along the bottom-trailing side of the screen. The following code example shows a simple implementation of an action that seeks the player forward to the time of the main content:

```swift
// Define an action to skip the intro of a media item.
private lazy var skipActions: [UIAction] = {
    [UIAction(title: "Skip Intro") { [weak self] _ in
        guard let self else { return }
        avPlayer.seek(to: skipToTime)
    }]
}()
```

When you set a value for the [`contextualActions`](avplayerviewcontroller/contextualactions.md) property, the player presents the controls immediately. To present them only during a relevant section of the content, observe the player timing by adding a periodic or boundary time observer. The following example defines a periodic time observer that fires every second during normal playback. In each invocation, it evaluates the new time to determine whether it falls within the presentation range. If it does, the example sets the skip action as the contextual actions value; otherwise, it clears the value by setting it to an empty array.

```swift
private func addTimeObserver() {
    // Observe the player's timing every second.
    let interval = CMTime(value: 1, timescale: 1)
    let fifteenSeconds = CMTime (value: 15, timescale: 1)
    timeObserver = avPlayer.addPeriodicTimeObserver(forInterval: interval,
                                                    queue: .main) { [weak self] time in
        guard let self else { return }
        let duration = avPlayer.currentItem?.duration ?? .zero
        // Show the Skip Intro button during the first 15 seconds of the content.
        showSkipIntroAction = time <= fifteenSeconds
    }
}
```

## See Also

- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md)
  Display standard controls in your app to edit the timeline of the currently playing media.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVExperienceController](avexperiencecontroller.md)
  An object that controls video experiences.
- [class AVMultiviewManager](avmultiviewmanager.md)
  An object that manages viewing multiple videos at once.
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVKit/adopting-the-system-player-interface-in-visionos)*