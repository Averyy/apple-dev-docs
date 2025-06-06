# parentWindow

**Framework**: GameKit  
**Kind**: property

The window that displays the dashboard.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBOutlet
@MainActor weak var parentWindow: NSWindow? { get set }
```

#### Discussion

Set this property before presenting a view controller. The window must be at least 800 x 600.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/parentwindow)*