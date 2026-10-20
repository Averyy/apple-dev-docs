# withMultiArray(_:)

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

> **Deprecated**: Use withMultiArray(for:) instead.

## Declaration

```swift
func withMultiArray<R>(_ body: (MLMultiArray) -> R) throws -> R
```

## See Also

### Getting a state buffer
- [func withMultiArray<R>(for: String, (MLMultiArray) throws -> R) rethrows -> R](./withmultiarray%28for,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlstate/withmultiarray(_:))*