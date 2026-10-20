# windowForSharingRequest(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Method called to get the window to share once sharing is confirmed, after a request is initiated by requestSharingOfWindowUsingPreview:title:completionHandler:. Implement this on the delegate of the requesting window

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
optional func windowForSharingRequest(from window: NSWindow) -> NSWindow?
```

```objc
- (NSWindow *) windowForSharingRequestFromWindow:(NSWindow *) window;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowforsharingrequest(from:))*