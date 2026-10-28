# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The track’s transform preference to apply to its visual content during presentation or processing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform> { get }
```

Available when `Root` inherits `AVAssetTrack`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading visual characteristics
- [static var naturalSize: AVAsyncProperty<Root, CGSize>](./naturalsize.md)
  The natural dimensions of the media data that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredtransform-90jdn)*