# navigateForward(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Navigates to the specific object.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func navigateForward(to object: Any)
```

```objc
- (void) navigateForwardToObject:(id) object;
```

## Discussion

Clears the [`arrangedObjects`](./arrangedobjects.md) array after the selected index, adds the argument to that array, and sets the [`selectedIndex`](./selectedindex.md) to the object’s index.

## Parameters

- `object`: The object to display.

## See Also

### Related Documentation
- [func takeSelectedIndexFrom(Any?)](./takeselectedindexfrom%28_%29.md)
  Navigates to the selected index, which is taken from the sender.
- [func navigateBack(Any?)](./navigateback%28_%29.md)
  Navigates backwards in the page controller’s arranged objects array.
- [func navigateForward(Any?)](./navigateforward%28_%29.md)
  Navigates to the next object in the page controller’s arranged objects array, if appropriate.
### Page Controller Items
- [var arrangedObjects: [Any]](./arrangedobjects.md)
  An array containing the objects displayed in the page controller’s view.
- [var selectedIndex: Int](./selectedindex.md)
  The currently selected object in the arranged objects array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/navigateforward(to:))*