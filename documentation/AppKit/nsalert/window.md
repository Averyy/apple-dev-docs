# window

**Framework**: AppKit  
**Kind**: property

The app-modal panel or document-modal sheet that corresponds to the alert.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var window: NSWindow { get }
```

#### Discussion

The alert’s window is of type [`NSPanel`](nspanel.md). Use this property when you want to dismiss an alert created with the [`beginSheetModal(for:completionHandler:)`](nsalert/beginsheetmodal(for:completionhandler:).md) method within that method’s completion handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/window)*