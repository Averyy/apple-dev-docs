# AVInterstitialTimeRange

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVInterstitialTimeRange
```

```objc
@interface AVInterstitialTimeRange : NSObject
```

## Mentions

- [Working with interstitial content](./working-with-interstitial-content.md)

#### Overview

When you associate interstitial time ranges with an [`AVPlayerItem`](../AVFoundation/avplayeritem.md) you present with an [`AVPlayerViewController`](./avplayerviewcontroller.md), you can customize or restrict the presentation of interstitial content. For example, you can allow the user to skip advertisements or prohibit skipping of a legal notice.

## Topics

### Creating an interstitial time range
- [init(timeRange: CMTimeRange)](./avinterstitialtimerange/init%28timerange%29.md)
  Initializes an interstitial time range object with the specified time range.
### Inspecting an interstitial time range
- [var timeRange: CMTimeRange](./avinterstitialtimerange/timerange.md)
  The time range identified as interstitial content.
### Initializers
- [init?(coder: NSCoder)](./avinterstitialtimerange/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Interstitials and markers
- [Working with interstitial content](./working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting navigation markers](./presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [class AVNavigationMarkersGroup](./avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterstitialtimerange)*