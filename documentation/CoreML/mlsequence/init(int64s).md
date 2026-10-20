# init(int64s:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a sequence of integers from an array of numbers.

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
convenience init(int64s int64Values: [NSNumber])
```

```objc
+ (instancetype) sequenceWithInt64Array:(NSArray<NSNumber *> *) int64Values;
```

## Parameters

- `int64Values`: An array of integer values represented as [`NSNumber`](../../Foundation/nsnumber.md) instances.

## See Also

### Creating a sequence
- [convenience init(strings: [String])](./init%28strings%29.md)
  Creates a sequence of strings from a string array.
- [convenience init(empty: MLFeatureType)](./init%28empty%29.md)
  Creates an empty sequence of strings or integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence/init(int64s:))*