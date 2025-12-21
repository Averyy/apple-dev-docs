# init(converting:)

**Framework**: Core ML  
**Kind**: init

Initialize by converting a MLMultiArray of different scalar type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(converting multiArray: MLMultiArray)
```

#### Discussion

Converting a floating number to an integer uses rounding-towards-zero method.

When necessary, the source values are truncated to fit the destination type, but the behavior is undefined if the source value is too large, too small, or otherwise not representable in the destination type.

## Parameters

- `multiArray`: MLMultiArray object

## See Also

- [init(MLMultiArray)](mlshapedarrayprotocol/init(_:).md)
  Creates a shaped array type from a multiarray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(converting:))*