# int64Values

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * int64Values;
```

## Discussion

Only use this property when the sequence’s [`type`](./type.md) is [`MLFeatureType.int64`](../mlfeaturetype/int64.md).

## See Also

### Retrieving the Sequence’s Values
- [var stringValues: [String]](./stringvalues.md)
  An array of strings in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence/int64values)*