# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The track’s transform preference to apply to its visual content during presentation or processing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var preferredTransform: CGAffineTransform { get }
```

#### Discussion

The value of this property is typically, but not always, [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md).

## See Also

### Accessing visual characteristics
- [var naturalSize: CGSize](./naturalsize.md)
  The natural dimensions of the media data that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/preferredtransform)*