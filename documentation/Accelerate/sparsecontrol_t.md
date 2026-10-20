# SparseControl_t

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Options that control the computation.

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
struct SparseControl_t
```

```c
typedef enum { ... } SparseControl_t;
```

## Topics

### Constants
- [var SparseDefaultControl: SparseControl_t](./sparsedefaultcontrol.md)
  A flag that indicates default values.
### Raw Values
- [init(UInt32)](./sparsecontrol_t/init%28_%29.md)
- [init(rawValue: UInt32)](./sparsecontrol_t/init%28rawvalue%29.md)
- [var rawValue: UInt32](./sparsecontrol_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Instance Properties
- [var control: SparseControl_t](./sparsenumericfactoroptions/control.md)
  The flags that control the computation.
- [var scalingMethod: SparseScaling_t](./sparsenumericfactoroptions/scalingmethod.md)
  The scaling method.
- [var scaling: UnsafeMutableRawPointer?](./sparsenumericfactoroptions/scaling.md)
  An array that scales the matrix before factorization.
- [struct SparseScaling_t](./sparsescaling_t.md)
  Options that define which scaling algorithm to use.
- [var pivotTolerance: Double](./sparsenumericfactoroptions/pivottolerance.md)
  The pivot tolerance that threshold partial pivoting uses.
- [var zeroTolerance: Double](./sparsenumericfactoroptions/zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecontrol_t)*