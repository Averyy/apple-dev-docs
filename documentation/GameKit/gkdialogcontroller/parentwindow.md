# parentWindow

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The window that displays the dashboard.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBOutlet
weak var parentWindow: NSWindow? { get set }
```

```objc
@property (weak, nullable) NSWindow * parentWindow;
```

## Discussion

Set this property before presenting a view controller. The window must be at least 800 x 600.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/parentwindow)*