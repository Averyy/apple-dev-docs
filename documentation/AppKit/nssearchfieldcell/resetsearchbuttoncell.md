# resetSearchButtonCell()

**Framework**: AppKit  
**Kind**: method

Resets the search button cell to its default attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resetSearchButtonCell()
```

#### Discussion

This method resets the target, action, regular image, and pressed image for the search button cell. By default, when users click the search button or press the Return key, the action defined for the receiver is sent to its designated target. This method gives you a way to customize the search button for specific situations and then reset the button defaults without having to undo changes individually.

## See Also

- [var searchButtonCell: NSButtonCell?](nssearchfieldcell/searchbuttoncell.md)
  The button cell used to display the search-button image.
- [var cancelButtonCell: NSButtonCell?](nssearchfieldcell/cancelbuttoncell.md)
  The button cell used to display the cancel-button image.
- [func resetCancelButtonCell()](nssearchfieldcell/resetcancelbuttoncell.md)
  Resets the cancel button cell to its default attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/resetsearchbuttoncell())*