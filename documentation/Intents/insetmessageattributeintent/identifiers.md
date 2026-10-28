# identifiers

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The array of message identifiers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var identifiers: [String]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * identifiers;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSString *> * identifiers;
```

## Discussion

Each string in this property corresponds to a message identifier that you use to locate the corresponding message in your app. The identifiers themselves are in the [`identifier`](../inmessage/identifier.md) property of an [`INMessage`](../inmessage.md) object returned during a search.

## See Also

### Getting the Attribute Details
- [var attribute: INMessageAttribute](./attribute.md)
  The attribute to apply to the messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintent/identifiers)*