# navigateForward(to:)

**Framework**: AppKit  
**Kind**: method

Navigates to the specific object.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func navigateForward(to object: Any)
```

#### Discussion

Clears the [`arrangedObjects`](nspagecontroller/arrangedobjects.md) array after the selected index, adds the argument to that array, and sets the [`selectedIndex`](nspagecontroller/selectedindex.md) to the object’s index.

## Parameters

- `object`: The object to display.

## See Also

- [func takeSelectedIndexFrom(Any?)](nspagecontroller/takeselectedindexfrom(_:).md)
  Navigates to the selected index, which is taken from the sender.
- [func navigateBack(Any?)](nspagecontroller/navigateback(_:).md)
  Navigates backwards in the page controller’s arranged objects array.
- [func navigateForward(Any?)](nspagecontroller/navigateforward(_:).md)
  Navigates to the next object in the page controller’s arranged objects array, if appropriate.
- [var arrangedObjects: [Any]](nspagecontroller/arrangedobjects.md)
  An array containing the objects displayed in the page controller’s view.
- [var selectedIndex: Int](nspagecontroller/selectedindex.md)
  The currently selected object in the arranged objects array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/navigateforward(to:))*