# close()

**Framework**: Quick Look  
**Kind**: method  
**Role**: Instance Method

Closes the preview session.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func close() async throws
```

#### Discussion

If the existing session is still open, this method closes it. The session’s events stream receives a `.didClose` event upon success.

> **Throws**: An `Error` if it is not possible to close the PreviewSession.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/previewsession/close())*