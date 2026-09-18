# Presenting navigation markers

**Framework**: AVKit

Present navigation markers in the Chapters panel to help users quickly navigate your content.

#### Overview

To help users navigate your content, the Chapters panel presents navigation markers that represent points of interest within the media’s timeline. Users can skip to desired content by selecting a marker with the Siri Remote.

![An image of Apple TV Chapters panel that shows a horizontal list of chapter markers.](/images/com.apple.avkit/media-3905733@2x.png)

#### Set the Navigation Markers

In tvOS, a [`AVPlayerItem`](https://developer.apple.com/documentation/avfoundation/avplayeritem) contains a [`navigationMarkerGroups`](https://developer.apple.com/documentation/avfoundation/avplayeritem/navigationmarkergroups) property you use to supply chapter information. Set this property to an array of [`AVNavigationMarkersGroup`](avnavigationmarkersgroup.md) objects to define the navigation markers for the current media.

> **Note**:  Although the player item defines the [`navigationMarkerGroups`](https://developer.apple.com/documentation/avfoundation/avplayeritem/navigationmarkergroups) property as an array, the system only supports the first group in the array.

An [`AVNavigationMarkersGroup`](avnavigationmarkersgroup.md) contains one or more [`AVTimedMetadataGroup`](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup) objects, each representing an individual marker presented in the player’s Info panel. Each [`AVTimedMetadataGroup`](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup) stores a time range in the asset’s timeline to which this marker applies, an array of [`AVMetadataItem`](https://developer.apple.com/documentation/avfoundation/avmetadataitem) objects to define the marker’s title, and, optionally, its thumbnail artwork.

![A top-down component diagram showing a player item containing navigation markers groups at the top. The middle component shows a navigation markers group containing timed metadata groups. The bottom component shows a timed metadata group containing multiple metadata items.](/images/com.apple.avkit/media-3905734@2x.png)

The following code shows how you can present a chapter list for your media:

```swift
struct Chapter {
    let title: String
    let imageName: String
    let startTime: TimeInterval
    let endTime: TimeInterval
}

...

func setupPlayback() {
    ...
    playerItem.navigationMarkerGroups = makeNavigationMarkerGroups()
    ...
}

private func makeNavigationMarkerGroups() -> [AVNavigationMarkersGroup] {
    
    let chapters = [
        Chapter(title: "Chapter 1", imageName: "chapter1", startTime: 0.0, endTime: 60.0),
        Chapter(title: "Chapter 2", imageName: "chapter2", startTime: 60.0, endTime: 120.0),
        Chapter(title: "Chapter 3", imageName: "chapter3", startTime: 120.0, endTime: 180.0),
        Chapter(title: "Chapter 4", imageName: "chapter4", startTime: 180.0, endTime: 240.0)
    ]
    
    var metadataGroups = [AVTimedMetadataGroup]()
    
    // Iterate over the defined chapters and build a timed metadata group object for each.
    chapters.forEach { chapter in
        metadataGroups.append(makeTimedMetadataGroup(for: chapter))
    }
    
    return [AVNavigationMarkersGroup(title: nil, 
                                     timedNavigationMarkers: metadataGroups)]
}

private func makeTimedMetadataGroup(for chapter: Chapter) -> AVTimedMetadataGroup {
    var metadata = [AVMetadataItem]()
    
    // Create a metadata item that contains the chapter title.
    let titleItem = makeMetadataItem(.commonIdentifierTitle, value: chapter.title)
    metadata.append(titleItem)
    if let image = UIImage(named: chapter.imageName), 
       let pngData = image.pngData() {
        // Create a metadata item that contains the chapter thumbnail.
        let imageItem = makeMetadataItem(.commonIdentifierArtwork, value: pngData)
        metadata.append(imageItem)
    }
    
    // Create a time range for the metadata group.
    let timescale: Int32 = 600
    let startTime = CMTime(seconds: chapter.startTime, preferredTimescale: timescale)
    let endTime = CMTime(seconds: chapter.endTime, preferredTimescale: timescale)
    let timeRange = CMTimeRangeFromTimeToTime(start: startTime, end: endTime)
    
    return AVTimedMetadataGroup(items: metadata, timeRange: timeRange)
}

private func makeMetadataItem(_ identifier: AVMetadataIdentifier, value: Any) -> AVMetadataItem {
    let item = AVMutableMetadataItem()
    item.identifier = identifier
    item.value = value as? NSCopying & NSObjectProtocol
    item.extendedLanguageTag = "und"
    return item.copy() as! AVMetadataItem
}

```

## See Also

- [Working with interstitial content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [class AVInterstitialTimeRange](avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [class AVNavigationMarkersGroup](avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/presenting-navigation-markers)*