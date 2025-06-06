# resetCancelButtonCell()

**Framework**: AppKit  
**Kind**: method

Resets the cancel button cell to its default attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resetCancelButtonCell()
```

#### Discussion

This method resets the target, action, regular image, and pressed image for the cancel button cell. By default, when users click the cancel button, the `delete:` action message is sent up the responder chain to the first `NSText` object that can handle it. This method gives you a way to customize the cancel button for specific situations and then reset the button defaults without having to undo changes individually.

## See Also

- [var searchButtonCell: NSButtonCell?](nssearchfieldcell/searchbuttoncell.md)
  The button cell used to display the search-button image.
- [func resetSearchButtonCell()](nssearchfieldcell/resetsearchbuttoncell.md)
  Resets the search button cell to its default attributes.
- [var cancelButtonCell: NSButtonCell?](nssearchfieldcell/cancelbuttoncell.md)
  The button cell used to display the cancel-button image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/resetcancelbuttoncell())*