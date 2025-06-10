# CNBoundsPrediction

**Framework**: Cinematic  
**Kind**: struct

A structure representing the bounds of the predicted subject.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
struct CNBoundsPrediction
```

## Topics

### Instance Properties
- [var confidence: Float](cnboundsprediction-swift.struct/confidence.md)
  A number between 0.0 and 1.0 representing the probability that a defined object is within the bounds.
- [var normalizedBounds: CGRect](cnboundsprediction-swift.struct/normalizedbounds.md)
  The bounds of the detected object in normalized coordinates where (0.0, 0.0) is the upper-left corner, and (1.0, 1.0) is the lower-right.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CNObjectTracker](cnobjecttracker-1n598.md)
  An object that converts a normalized point or rectangle into a detection track that tracks an object over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnboundsprediction-swift.struct)*