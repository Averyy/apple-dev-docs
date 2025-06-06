# setDelegate(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the delegate for this authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setDelegate(_ delegate: Any!)
```

#### Discussion

If you want to be notified of state changes (for example, when the user clicks the button), set a delegate and implement the delegate methods described in the delegate methods section.

## Parameters

- `delegate`: The object to which messages about the state of the authorization object should be sent.

## See Also

- [func delegate() -> Any!](sfauthorizationview/delegate.md)
  Returns the delegate for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setdelegate(_:))*