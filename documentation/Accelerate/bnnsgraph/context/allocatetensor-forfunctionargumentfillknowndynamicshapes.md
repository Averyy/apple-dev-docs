# allocateTensor(forFunction:argument:fillKnownDynamicShapes:)

**Framework**: Accelerate  
**Kind**: method

Returns an allocated tensor for a given function argument.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func allocateTensor(forFunction function: String? = nil, argument: String, fillKnownDynamicShapes: Bool) -> BNNSTensor?
```

#### Discussion

> **Note**: This function supports `Float`, `Float16`, `Bool`, and `Int32` datatypes only and returns `nil` for other types.

> **Note**: `BNNSGraphContextGetTensor`

## Parameters

- `function`: The specific function to create the tensor for. You may set this to   if there is only one function.
- `argument`: The argument to create the tensor for.
- `fillKnownDynamicShapes`: If  , the function replaces any dynamic shapes   with shapes that will be used on next execution of  , either drawn from default shapes in the    function or supplied by a preceding call to    or  .   Otherwise the function represents dynamically-sized dimensions with a value of   in either shape or stride as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/allocatetensor(forfunction:argument:fillknowndynamicshapes:))*