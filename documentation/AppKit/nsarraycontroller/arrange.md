# arrange(_:)

**Framework**: AppKit  
**Kind**: method

Returns a given array, appropriately sorted and filtered.

**Availability**:
- macOS ?+

## Declaration

```swift
func arrange(_ objects: [Any]) -> [Any]
```

#### Return Value

An array containing `objects` filtered using the receiver’s filter predicate (see [`filterPredicate`](nsarraycontroller/filterpredicate.md)) and sorted according to the receiver’s [`sortDescriptors`](nsarraycontroller/sortdescriptors.md).

#### Discussion

Subclasses should override this method to use a different sort mechanism, provide custom object arrangement, or (typically only prior to OS X version 10.4, which provides a filter predicate) filter the objects.

## See Also

- [var arrangedObjects: Any](nsarraycontroller/arrangedobjects.md)
  An array containing the receiver’s content objects arranged using [`arrange(_:)`](nsarraycontroller/arrange(_:).md).
- [func rearrangeObjects()](nsarraycontroller/rearrangeobjects.md)
  Triggers filtering of the receiver’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/arrange(_:))*