# locale

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The locale for the displayed messages. If `nil`, the user’s current locale is used. By default, this value is the current locale of the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var locale: Locale! { get set }
```

```objc
@property (null_resettable) NSLocale * locale;
```

## See Also

### Configuring Messages
- [var pinMessageIndices: [NSNumber]?](./pinmessageindices.md)
  A list of message indices referring to a predefined message table, used to specify the type and number of messages displayed during the PIN operation. `nil` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/locale)*