# makeArray(of:)

**Framework**: Accelerate  
**Kind**: method

Returns an array that contains a copy of this `BNNSTensor`’s elements.

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
func makeArray<T>(of scalarType: T.Type) -> [T] where T : BNNSScalar
```

## Parameters

- `scalarType`: The type that the tensor’s memory is bound to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor/makearray(of:))*