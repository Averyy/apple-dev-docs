# naturalSize

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The natural dimensions of the media data that the track references.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`naturalSize`](../avpartialasyncproperty/naturalsize.md) asynchronously instead.

## Declaration

```swift
var naturalSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize naturalSize;
```

#### Discussion

For visual tracks, like video or subtitle tracks, this property value is the natural size of the media. For nonvisual tracks, like audio or chapter tracks, the value is [`zero`](../../CoreFoundation/cgsize/zero.md).

## See Also

### Accessing visual characteristics
- [preferredTransform](./preferredtransform.md)
  The track’s transform preference to apply to its visual content during presentation or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/naturalsize)*