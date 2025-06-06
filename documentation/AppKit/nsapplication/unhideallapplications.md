# unhideAllApplications(_:)

**Framework**: AppKit  
**Kind**: method

Unhides all apps, including the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func unhideAllApplications(_ sender: Any?)
```

#### Discussion

This action causes each app to order its windows to the front, which could obscure the currently active window in the active app.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func hideOtherApplications(Any?)](nsapplication/hideotherapplications(_:).md)
  Hides all apps, except the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unhideallapplications(_:))*