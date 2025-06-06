# alertMessage

**Framework**: Core NFC  
**Kind**: property

A message to show on the alert action sheet after card emulation starts.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var alertMessage: String { get set }
```

#### Discussion

Use this string to provide additional context about the NFC card emulation process. You can update this string in any thread context as long as the session is valid. Set this value prior to calling [`startEmulation()`](cardsession/startemulation().md) to display an appropriate message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/alertmessage)*