# selectedViewController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view controller associated with the selected object..

**Availability**:
- macOS 10.8+

## Declaration

```swift
var selectedViewController: NSViewController? { get }
```

```objc
@property (strong, readonly, nullable) NSViewController * selectedViewController;
```

## Discussion

May be `nil` if not using view controllers.

This property is only relevant in book mode. See [Book Mode (View Controller Mode)](../nspagecontroller.md#Book-Mode-View-Controller-Mode) for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/selectedviewcontroller)*