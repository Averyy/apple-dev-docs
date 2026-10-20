# invalidate()

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Closes the reader session, which prevents it from being reused.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidateSession;
```

## See Also

### Managing a Reader Session
- [func begin()](./begin%28%29.md)
  Starts the reader session.
- [func invalidate(errorMessage: String)](./invalidate%28errormessage%29.md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](./alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.
- [func begin()](./begin%28%29.md)
  Starts the reader session.
- [func invalidate(errorMessage: String)](./invalidate%28errormessage%29.md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](./alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol/invalidate())*