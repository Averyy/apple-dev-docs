# CTRunStatus

**Framework**: Core Text  
**Kind**: struct  
**Role**: Structure

A bitfield that represents the disposition of the run.

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
struct CTRunStatus
```

```c
enum CTRunStatus : uint32_t;
```

#### Overview

The [`CTRunGetStatus(_:)`](./ctrungetstatus%28_%29.md) function passes back this bitfield to indicate the disposition of the run.

## Topics

### Constants
- [static var rightToLeft: CTRunStatus](./ctrunstatus/righttoleft.md)
  The run proceeds from right to left.
- [static var nonMonotonic: CTRunStatus](./ctrunstatus/nonmonotonic.md)
  The run isn’t in strictly increasing or decreasing order.
- [static var hasNonIdentityMatrix: CTRunStatus](./ctrunstatus/hasnonidentitymatrix.md)
  The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.
### Initializers
- [init(rawValue: UInt32)](./ctrunstatus/init%28rawvalue%29.md)
  Creates a run status structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrunstatus)*