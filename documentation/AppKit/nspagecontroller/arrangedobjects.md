# arrangedObjects

**Framework**: AppKit  
**Kind**: property

An array containing the objects displayed in the page controller’s view.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var arrangedObjects: [Any] { get set }
```

#### Discussion

The delegate will be asked for snapshots as they are needed. Alternatively, you may never directly set this array and use the -[`navigateForward(to:)`](nspagecontroller/navigateforward(to:).md) method to create a history as the user navigates.

This property is key-value observing compliant.

## See Also

- [func navigateForward(to: Any)](nspagecontroller/navigateforward(to:).md)
  Navigates to the specific object.
- [var selectedIndex: Int](nspagecontroller/selectedindex.md)
  The currently selected object in the arranged objects array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/arrangedobjects)*