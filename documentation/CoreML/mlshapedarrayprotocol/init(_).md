# init(_:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array type from a multiarray.

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
init(_ multiArray: MLMultiArray)
```

## Parameters

- `multiArray`: An [`MLMultiArray`](../mlmultiarray.md) with the same underlying type as the shaped array type.

## See Also

### Creating a shaped array type from another type
- [init(converting:)](./init%28converting%29.md)
  Initialize by converting a MLMultiArray of different scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(_:))*