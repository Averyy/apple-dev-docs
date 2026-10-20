# init(strings:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a sequence of strings from a string array.

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
convenience init(strings stringValues: [String])
```

```objc
+ (instancetype) sequenceWithStringArray:(NSArray<NSString *> *) stringValues;
```

## Parameters

- `stringValues`: The array of strings for the sequence.

## See Also

### Creating a sequence
- [convenience init(int64s: [NSNumber])](./init%28int64s%29.md)
  Creates a sequence of integers from an array of numbers.
- [convenience init(empty: MLFeatureType)](./init%28empty%29.md)
  Creates an empty sequence of strings or integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence/init(strings:))*