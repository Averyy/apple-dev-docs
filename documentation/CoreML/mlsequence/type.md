# type

**Framework**: Core ML  
**Kind**: property

The underlying type of the sequence’s elements.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var type: MLFeatureType { get }
```

#### Discussion

The sequence’s underlying element type can only be either [`MLFeatureType.string`](mlfeaturetype/string.md) or [`MLFeatureType.int64`](mlfeaturetype/int64.md). Use this value to determine whether to access [`stringValues`](mlsequence/stringvalues.md) or [`int64Values`](mlsequence/int64values.md) at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence/type)*