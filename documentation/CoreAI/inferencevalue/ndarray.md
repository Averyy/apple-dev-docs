# ndArray

**Framework**: Core AI  
**Kind**: property

The array that the value wraps.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var ndArray: NDArray? { get }
```

#### Discussion

This property is `nil` when the value contains an image instead of an array. Accessing this property consumes the value and transfers ownership of the array to the caller.

## See Also

- [var kind: InferenceValue.Kind](inferencevalue/kind-swift.property.md)
  The kind of data this value contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/ndarray)*