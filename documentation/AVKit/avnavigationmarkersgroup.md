# AVNavigationMarkersGroup

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A set of markers for navigating playback of an audiovisual presentation.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class AVNavigationMarkersGroup
```

```objc
@interface AVNavigationMarkersGroup : NSObject
```

## Mentions

- [Presenting navigation markers](./presenting-navigation-markers.md)

#### Overview

The most common form of a navigation markers group is a chapter list; however, you can also provide other sets of markers to allow a user to jump to significant events in the presentation. For example, a “Goals Scored” markers group might summarize key moments in a recorded sporting event. When you associate navigation markers with an [`AVPlayerItem`](../AVFoundation/avplayeritem.md) object you present with an [`AVPlayerViewController`](./avplayerviewcontroller.md), the user interface provides options for navigating each group.

## Topics

### Creating a navigation marker group
- [init(title: String?, timedNavigationMarkers: [AVTimedMetadataGroup])](./avnavigationmarkersgroup/init%28title,timednavigationmarkers%29.md)
  Initializes a navigation markers group with the specified title and array of timed navigation markers.
- [init(title: String?, dateRangeNavigationMarkers: [AVDateRangeMetadataGroup])](./avnavigationmarkersgroup/init%28title,daterangenavigationmarkers%29.md)
  Initializes a navigation markers group with the specified title and array of date range navigation markers.
### Inspecting navigation metadata
- [var title: String?](./avnavigationmarkersgroup/title.md)
  The title of the marker group.
- [var timedNavigationMarkers: [AVTimedMetadataGroup]?](./avnavigationmarkersgroup/timednavigationmarkers.md)
  The array of timed navigation markers for which the group provides navigation.
- [var dateRangeNavigationMarkers: [AVDateRangeMetadataGroup]?](./avnavigationmarkersgroup/daterangenavigationmarkers.md)
  The array of date range navigation markers for which the group provides navigation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Interstitials and markers
- [Working with interstitial content](./working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting navigation markers](./presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [class AVInterstitialTimeRange](./avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup)*