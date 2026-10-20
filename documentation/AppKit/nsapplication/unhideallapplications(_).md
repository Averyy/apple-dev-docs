# unhideAllApplications(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unhides all apps, including the receiver.

**Availability**:
- macOS

## Declaration

```swift
func unhideAllApplications(_ sender: Any?)
```

```objc
- (void) unhideAllApplications:(id) sender;
```

#### Discussion

This action causes each app to order its windows to the front, which could obscure the currently active window in the active app.

## Parameters

- `sender`: The object that sent this message.

## See Also

### Hiding apps
- [func hideOtherApplications(Any?)](./hideotherapplications%28_%29.md)
  Hides all apps, except the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unhideallapplications(_:))*