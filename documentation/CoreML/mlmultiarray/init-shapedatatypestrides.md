# init(shape:dataType:strides:)

**Framework**: Core ML  
**Kind**: init

Creates the object with specified strides.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])
```

#### Discussion

The contents of the object are left uninitialized; the client must initialize it.

## Parameters

- `shape`: The shape
- `dataType`: The data type
- `strides`: The strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(shape:datatype:strides:))*