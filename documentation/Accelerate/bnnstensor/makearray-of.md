# makeArray(of:)

**Framework**: Accelerate  
**Kind**: method

Returns an array that contains a copy of this `BNNSTensor`’s elements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func makeArray<T>(of scalarType: T.Type) -> [T] where T : BNNSScalar
```

## Parameters

- `scalarType`: The type that the tensor’s memory is bound to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/makearray(of:))*