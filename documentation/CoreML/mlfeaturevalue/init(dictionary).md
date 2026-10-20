# init(dictionary:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a feature value that contains a dictionary of numbers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(dictionary value: [AnyHashable : NSNumber]) throws
```

```objc
+ (instancetype) featureValueWithDictionary:(NSDictionary<id,NSNumber *> *) value error:(NSError **) error;
```

## Parameters

- `value`: A dictionary of numbers.

## See Also

### Creating collection feature values
- [convenience init(sequence: MLSequence)](./init%28sequence%29.md)
  Creates a feature value that contains a sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/init(dictionary:))*