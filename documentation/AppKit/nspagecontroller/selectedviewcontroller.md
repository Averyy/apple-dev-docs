# selectedViewController

**Framework**: AppKit  
**Kind**: property

The view controller associated with the selected object..

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var selectedViewController: NSViewController? { get }
```

#### Discussion

May be `nil` if not using view controllers.

This property is only relevant in book mode. See [`Book Mode (View Controller Mode)`](nspagecontroller#Book-Mode-View-Controller-Mode.md) for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/selectedviewcontroller)*