# preferredTransform

**Framework**: AVFoundation  
**Kind**: property

The track’s transform preference to apply to its visual content during presentation or processing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var preferredTransform: CGAffineTransform { get }
```

#### Discussion

The value of this property is typically, but not always, [`CGAffineTransformIdentity`](https://developer.apple.com/documentation/coregraphics/cgaffinetransformidentity).

## See Also

- [var naturalSize: CGSize](avcompositiontrack/naturalsize.md)
  The natural dimensions of the media data that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/preferredtransform)*