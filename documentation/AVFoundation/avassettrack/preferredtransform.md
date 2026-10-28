# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The track’s transform preference to apply to its visual content during presentation or processing.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`preferredTransform`](../avpartialasyncproperty/preferredtransform-90jdn.md) asynchronously instead.

## Declaration

```swift
var preferredTransform: CGAffineTransform { get }
```

```objc
@property (nonatomic, readonly) CGAffineTransform preferredTransform;
```

## Discussion

The value of this property is typically, but not always, [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md).

## See Also

### Accessing visual characteristics
- [naturalSize](./naturalsize.md)
  The natural dimensions of the media data that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/preferredtransform)*