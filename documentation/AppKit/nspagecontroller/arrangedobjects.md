# arrangedObjects

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the objects displayed in the page controller’s view.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var arrangedObjects: [Any] { get set }
```

```objc
@property (copy) NSArray * arrangedObjects;
```

## Discussion

The delegate will be asked for snapshots as they are needed. Alternatively, you may never directly set this array and use the -[`navigateForward(to:)`](./navigateforward%28to%29.md) method to create a history as the user navigates.

This property is key-value observing compliant.

## See Also

### Page Controller Items
- [func navigateForward(to: Any)](./navigateforward%28to%29.md)
  Navigates to the specific object.
- [var selectedIndex: Int](./selectedindex.md)
  The currently selected object in the arranged objects array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/arrangedobjects)*