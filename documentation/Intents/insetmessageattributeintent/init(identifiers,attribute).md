# init(identifiers:attribute:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the set message attribute intent object with the specified identifiers and attribute.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(identifiers: [String]?, attribute: INMessageAttribute)
```

```objc
- (instancetype) initWithIdentifiers:(NSArray<NSString *> *) identifiers attribute:(INMessageAttribute) attribute;
```

## Return Value

An initialized intent or `nil` if the object could not be created.

## Discussion

Typically, you don’t create instances of this class yourself. Siri creates instances when the user asks to modify the attributes of one or more messages. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `identifiers`: An array of identifier strings representing the messages to modify. Each string represents the [`identifier`](../inmessage/identifier.md) of an [`INMessage`](../inmessage.md) object that you provided previously.
- `attribute`: The attribute to apply to the messages. For a list of possible values, see [`INMessageAttribute`](../inmessageattribute.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintent/init(identifiers:attribute:))*