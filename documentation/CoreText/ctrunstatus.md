# CTRunStatus

**Framework**: Core Text  
**Kind**: struct

A bitfield that represents the disposition of the run.

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
struct CTRunStatus
```

#### Overview

The [`CTRunGetStatus(_:)`](ctrungetstatus(_:).md) function passes back this bitfield to indicate the disposition of the run.

## Topics

### Constants
- [static var rightToLeft: CTRunStatus](ctrunstatus/righttoleft.md)
  The run proceeds from right to left.
- [static var nonMonotonic: CTRunStatus](ctrunstatus/nonmonotonic.md)
  The run isn’t in strictly increasing or decreasing order.
- [static var hasNonIdentityMatrix: CTRunStatus](ctrunstatus/hasnonidentitymatrix.md)
  The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.
### Initializers
- [init(rawValue: UInt32)](ctrunstatus/init(rawvalue:).md)
  Creates a run status structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrunstatus)*