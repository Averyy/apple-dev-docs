# rearrangeObjects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Triggers filtering of the receiver’s content.

**Availability**:
- macOS

## Declaration

```swift
func rearrangeObjects()
```

```objc
- (void) rearrangeObjects;
```

#### Discussion

This method invokes [`arrange(_:)`](./arrange%28_%29.md).

When you detect that filtering criteria change (such as when listening to the text sent by an `NSSearchField` instance), invoke this method on `self`.

## See Also

### Related Documentation
- [func didChangeArrangementCriteria()](./didchangearrangementcriteria%28%29.md)
  Invoked when any criteria for arranging objects change.
### Arranging Objects
- [func arrange([Any]) -> [Any]](./arrange%28_%29.md)
  Returns a given array, appropriately sorted and filtered.
- [var arrangedObjects: Any](./arrangedobjects.md)
  An array containing the receiver’s content objects arranged using [`arrange(_:)`](./arrange%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/rearrangeobjects())*