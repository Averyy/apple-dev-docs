# naturalSize

**Framework**: AVFoundation  
**Kind**: property

The natural dimensions of the media data that the track references.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var naturalSize: AVAsyncProperty<Root, CGSize> { get }
```

#### Discussion

Use the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method to retrieve the property value.

For visual tracks, like video or subtitle tracks, this property value is the natural size of the media. For nonvisual tracks, like audio or chapter tracks, the value is [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGSize/zero).

## See Also

- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](avpartialasyncproperty/preferredtransform-90jdn.md)
  The track’s transform preference to apply to its visual content during presentation or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/naturalsize)*