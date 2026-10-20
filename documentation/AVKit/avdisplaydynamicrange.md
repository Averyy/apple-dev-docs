# AVDisplayDynamicRange

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Describes how High Dynamic Range (HDR) video content renders.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum AVDisplayDynamicRange
```

```c
enum AVDisplayDynamicRange : NSInteger;
```

## Topics

### Creating a dynamic range
- [init?(rawValue: Int)](./avdisplaydynamicrange/init%28rawvalue%29.md)
### Dynamic ranges
- [AVDisplayDynamicRange.automatic](./avdisplaydynamicrange/automatic.md)
  Defines an automatic dynamic range. Indicates that the dynamic range will be set automatically.
- [AVDisplayDynamicRange.standard](./avdisplaydynamicrange/standard.md)
  Defines a standard dynamic range. Restricts the video content dynamic range to the standard range regardless of the actual range of the video content.
- [AVDisplayDynamicRange.constrainedHigh](./avdisplaydynamicrange/constrainedhigh.md)
  Defines a constrained high dynamic range. Allows for constrained High Dynamic Range (HDR) video content which is useful for mixing HDR and Standard Dynamic Range (SDR) content.
- [AVDisplayDynamicRange.high](./avdisplaydynamicrange/high.md)
  Defines a high dynamic range. Allows video content to use extended dynamic range if it has dynamic range content.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Display management
- [class AVDisplayManager](./avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaydynamicrange)*