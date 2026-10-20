# init(empty:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates an empty sequence of strings or integers.

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
convenience init(empty type: MLFeatureType)
```

```objc
+ (instancetype) emptySequenceWithType:(MLFeatureType) type;
```

## Parameters

- `type`: An [`MLFeatureType`](../mlfeaturetype.md) instance that determines the sequence’s element type, which must be either [`MLFeatureType.string`](../mlfeaturetype/string.md) or [`MLFeatureType.int64`](../mlfeaturetype/int64.md).

## See Also

### Creating a sequence
- [convenience init(strings: [String])](./init%28strings%29.md)
  Creates a sequence of strings from a string array.
- [convenience init(int64s: [NSNumber])](./init%28int64s%29.md)
  Creates a sequence of integers from an array of numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence/init(empty:))*