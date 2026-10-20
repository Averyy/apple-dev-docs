# begin()

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Starts the reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func begin()
```

```objc
- (void) beginSession;
```

## See Also

### Managing a Reader Session
- [func invalidate()](./invalidate%28%29.md)
  Closes the reader session, which prevents it from being reused.
- [func invalidate(errorMessage: String)](./invalidate%28errormessage%29.md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](./alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.
- [func invalidate()](./invalidate%28%29.md)
  Closes the reader session, which prevents it from being reused.
- [func invalidate(errorMessage: String)](./invalidate%28errormessage%29.md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](./alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol/begin())*