# pinMessageIndices

**Framework**: CryptoTokenKit  
**Kind**: property

A list of message indices referring to a predefined message table, used to specify the type and number of messages displayed during the PIN operation. `nil` by default.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var pinMessageIndices: [NSNumber]? { get set }
```

#### Discussion

If `nil`, the reader does not display any message (reader specific). Typically, PIN verification takes 1 message; PIN modification takes 1 – 3 messages.

## See Also

- [var locale: Locale!](tksmartcarduserinteractionforpinoperation/locale.md)
  The locale for the displayed messages. If `nil`, the user’s current locale is used. By default, this value is the current locale of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/pinmessageindices)*