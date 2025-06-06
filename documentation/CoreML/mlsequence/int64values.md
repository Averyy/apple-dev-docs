# int64Values

**Framework**: Core ML  
**Kind**: property

An array of 64-bit integers in the sequence.

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
var int64Values: [NSNumber] { get }
```

#### Discussion

Only use this property when the sequence’s [`type`](mlsequence/type.md) is [`MLFeatureType.int64`](mlfeaturetype/int64.md).

## See Also

- [var stringValues: [String]](mlsequence/stringvalues.md)
  An array of strings in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence/int64values)*