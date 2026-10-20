# init(identifier:title:type:)

**Framework**: ClassKit  
**Kind**: init  
**Role**: Initializer

Initializes a new binary activity item of the given type.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(identifier: String, title: String, type valueType: CLSBinaryValueType)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier title:(NSString *) title type:(CLSBinaryValueType) valueType;
```

## Parameters

- `identifier`: A unique identifier for the activity item.
- `title`: A human readable name for the activity item.
- `valueType`: The kind of Boolean that the activity item represents.

## See Also

### Creating Binary Activity Items
- [enum CLSBinaryValueType](../clsbinaryvaluetype.md)
  The kinds of outcomes that a binary activity item can represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsbinaryitem/init(identifier:title:type:))*