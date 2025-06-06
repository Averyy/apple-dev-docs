# windowForSharingRequest(from:)

**Framework**: AppKit  
**Kind**: method

Method called to get the window to share once sharing is confirmed, after a request is initiated by requestSharingOfWindowUsingPreview:title:completionHandler:. Implement this on the delegate of the requesting window

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
optional func windowForSharingRequest(from window: NSWindow) -> NSWindow?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowforsharingrequest(from:))*