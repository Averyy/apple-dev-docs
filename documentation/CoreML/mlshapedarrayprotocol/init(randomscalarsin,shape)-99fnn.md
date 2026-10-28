# init(randomScalarsIn:shape:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array type that initializes the elements to random integer values within a range.

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
init(randomScalarsIn range: Range<Self.Scalar>, shape: [Int])
```

Available when `Scalar` conforms to `FixedWidthInteger`.

**Other overloads**:

```swift
init(randomScalarsIn range: Range<Self.Scalar>, shape: [Int])
```

## Parameters

- `range`: A range of integer values.
- `shape`: An integer array. Each element represents the size of the shaped array’s corresponding dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(randomscalarsin:shape:)-99fnn)*