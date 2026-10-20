# SparseIterativeMethod

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

The base type for all iterative methods.

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
struct SparseIterativeMethod
```

```c
typedef struct { ... } SparseIterativeMethod;
```

## Topics

### Initializers
- [init(method: Int32, options: SparseIterativeMethod.__Unnamed_union_options)](./sparseiterativemethod/init%28method,options%29.md)
  Returns a new iterative method structure with the specified method and options.
- [init()](./sparseiterativemethod/init%28%29.md)
  Returns a new iterative method structure.
### Instance Properties
- [var method: Int32](./sparseiterativemethod/method.md)
  The iterative method this structure represents.
- [var options: SparseIterativeMethod.__Unnamed_union_options](./sparseiterativemethod/options.md)
  The options for the method.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterativemethod)*