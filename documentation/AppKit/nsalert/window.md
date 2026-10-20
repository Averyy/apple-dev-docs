# window

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The app-modal panel or document-modal sheet that corresponds to the alert.

**Availability**:
- macOS

## Declaration

```swift
var window: NSWindow { get }
```

```objc
@property (strong, readonly) NSWindow * window;
```

#### Discussion

The alert’s window is of type [`NSPanel`](../nspanel.md). Use this property when you want to dismiss an alert created with the [`beginSheetModal(for:completionHandler:)`](./beginsheetmodal%28for,completionhandler%29.md) method within that method’s completion handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/window)*