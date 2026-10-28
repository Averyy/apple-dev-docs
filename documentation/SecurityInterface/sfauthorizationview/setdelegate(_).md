# setDelegate(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the delegate for this authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setDelegate(_ delegate: Any!)
```

```objc
- (void) setDelegate:(id) delegate;
```

## Discussion

If you want to be notified of state changes (for example, when the user clicks the button), set a delegate and implement the delegate methods described in the delegate methods section.

## Parameters

- `delegate`: The object to which messages about the state of the authorization object should be sent.

## See Also

### Setting and getting the delegate for the view
- [func delegate() -> Any!](./delegate%28%29.md)
  Returns the delegate for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setdelegate(_:))*