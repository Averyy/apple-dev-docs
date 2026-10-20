# invalidate()

**Framework**: Core NFC  
**Kind**: method  
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

## See Also

- [func begin()](nfcreadersessionprotocol/begin.md)
  Starts the reader session.
- [func invalidate(errorMessage: String)](nfcreadersessionprotocol/invalidate(errormessage:).md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](nfcreadersessionprotocol/alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.
- [func begin()](nfcreadersessionprotocol/begin.md)
  Starts the reader session.
- [func invalidate(errorMessage: String)](nfcreadersessionprotocol/invalidate(errormessage:).md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](nfcreadersessionprotocol/alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol/invalidate())*