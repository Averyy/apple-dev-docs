# withMultiArray(for:_:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func withMultiArray<R>(for stateName: String, _ body: (MLMultiArray) throws -> R) rethrows -> R
```

## See Also

### Getting a state buffer
- [func withMultiArray<R>((MLMultiArray) -> R) throws -> R](./withmultiarray%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlstate/withmultiarray(for:_:))*