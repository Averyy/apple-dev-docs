# CTFramePathFillRule

**Framework**: Core Text  
**Kind**: enum

These constants specify the fill rule used by a frame

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
enum CTFramePathFillRule
```

#### Overview

When a path intersects with itself, the client should specify which rule to use for deciding the area of the path.

## Topics

### Enumeration Cases
- [CTFramePathFillRule.evenOdd](ctframepathfillrule/evenodd.md)
  Paints the area using the even-odd fill rule.
- [CTFramePathFillRule.windingNumber](ctframepathfillrule/windingnumber.md)
  Paints the area using the nonzero winding number rule.
### Initializers
- [init?(rawValue: UInt32)](ctframepathfillrule/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframepathfillrule)*