# init(identityMatrixOfSize:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array type that’s an identity matrix of integers.

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

Available when `Scalar` conforms to `FixedWidthInteger`.

**Other overloads**:

```swift
init(identityMatrixOfSize size: Int)
```

## Parameters

- `size`: The size of the identity matrix. For example, a size of `5` creates a 5x5 identity matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(identitymatrixofsize:)-77y0e)*