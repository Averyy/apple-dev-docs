# CTFramePathFillRule

**Framework**: Core Text  
**Kind**: enum  
**Role**: Enumeration

These constants specify the fill rule used by a frame

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
enum CTFramePathFillRule
```

```c
enum CTFramePathFillRule : uint32_t;
```

#### Overview

When a path intersects with itself, the client should specify which rule to use for deciding the area of the path.

## Topics

### Enumeration Cases
- [CTFramePathFillRule.evenOdd](./ctframepathfillrule/evenodd.md)
  Paints the area using the even-odd fill rule.
- [CTFramePathFillRule.windingNumber](./ctframepathfillrule/windingnumber.md)
  Paints the area using the nonzero winding number rule.
### Initializers
- [init?(rawValue: UInt32)](./ctframepathfillrule/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframepathfillrule)*