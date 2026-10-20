# invalidate(errorMessage:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Closes the reader session and displays an error message to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func invalidate(errorMessage: String)
```

```objc
- (void) invalidateSessionWithErrorMessage:(NSString *) errorMessage;
```

#### Discussion

Use this method to end the reader session and display a message to the user when an error condition occurs after the app successfully reads a tag. This type of error can occur if, for example, the app reads data from an NFC tag, but determines that the data has expired and discards it. The app then calls [`invalidate(errorMessage:)`](./invalidate%28errormessage%29.md) to end the reader session, and to let the user know why it discarded the data.

> **Note**:  After invalidating a reader session, you cannot use it to scan and detect other tags.

## Parameters

- `errorMessage`: The error message to display.

## See Also

### Managing a Reader Session
- [func begin()](./begin%28%29.md)
  Starts the reader session.
- [func invalidate()](./invalidate%28%29.md)
  Closes the reader session, which prevents it from being reused.
- [var alertMessage: String](./alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.
- [func begin()](./begin%28%29.md)
  Starts the reader session.
- [func invalidate()](./invalidate%28%29.md)
  Closes the reader session, which prevents it from being reused.
- [var alertMessage: String](./alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol/invalidate(errormessage:))*