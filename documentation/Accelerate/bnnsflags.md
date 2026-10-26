# BNNSFlags

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Options that control the behavior of a filter parameter.

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
struct BNNSFlags
```

```c
typedef enum { ... } BNNSFlags;
```

## Topics

### Filter Flags
- [static var useClientPointer: BNNSFlags](./bnnsflags/useclientpointer.md)
  A flag that instructs the filter to use pointers to data you provide at creation time.
### Raw Values
- [init(UInt32)](./bnnsflags/init%28_%29.md)
- [var rawValue: UInt32](./bnnsflags/rawvalue.md)
- [BNNSFlagsUseClientPtr](./bnnsflags/bnnsflagsuseclientptr.md)
  A flag that instructs the filter to use pointers to data you provide at creation time.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Hashable](../Swift/hashable.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsflags)*