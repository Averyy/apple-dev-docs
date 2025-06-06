# init(identityMatrixOfSize:)

**Framework**: Core ML  
**Kind**: init

Initialize as an identity matrix.

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
init(identityMatrixOfSize size: Int)
```

#### Discussion

The initializer creates a shaped array of shape size x size where the contents are zeros except array[scalarAt: x, x], which are ones.

## Parameters

- `size`: The size (order) of the matrix


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(identitymatrixofsize:)-1xx88)*