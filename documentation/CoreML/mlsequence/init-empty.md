# init(empty:)

**Framework**: Core ML  
**Kind**: init

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

## Parameters

- `type`: An   instance that determines the sequence’s element type, which must be either   or  .

## See Also

- [convenience init(strings: [String])](mlsequence/init(strings:).md)
  Creates a sequence of strings from a string array.
- [convenience init(int64s: [NSNumber])](mlsequence/init(int64s:).md)
  Creates a sequence of integers from an array of numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence/init(empty:))*