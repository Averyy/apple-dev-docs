# rearrangeObjects()

**Framework**: AppKit  
**Kind**: method

Triggers filtering of the receiver’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
func rearrangeObjects()
```

#### Discussion

This method invokes [`arrange(_:)`](nsarraycontroller/arrange(_:).md).

When you detect that filtering criteria change (such as when listening to the text sent by an `NSSearchField` instance), invoke this method on `self`.

## See Also

- [func didChangeArrangementCriteria()](nsarraycontroller/didchangearrangementcriteria.md)
  Invoked when any criteria for arranging objects change.
- [func arrange([Any]) -> [Any]](nsarraycontroller/arrange(_:).md)
  Returns a given array, appropriately sorted and filtered.
- [var arrangedObjects: Any](nsarraycontroller/arrangedobjects.md)
  An array containing the receiver’s content objects arranged using [`arrange(_:)`](nsarraycontroller/arrange(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/rearrangeobjects())*