# arrange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a given array, appropriately sorted and filtered.

**Availability**:
- macOS

## Declaration

```swift
func arrange(_ objects: [Any]) -> [Any]
```

```objc
- (NSArray *) arrangeObjects:(NSArray *) objects;
```

#### Return Value

An array containing `objects` filtered using the receiver’s filter predicate (see [`filterPredicate`](./filterpredicate.md)) and sorted according to the receiver’s [`sortDescriptors`](./sortdescriptors.md).

#### Discussion

Subclasses should override this method to use a different sort mechanism, provide custom object arrangement, or (typically only prior to OS X version 10.4, which provides a filter predicate) filter the objects.

## See Also

### Arranging Objects
- [var arrangedObjects: Any](./arrangedobjects.md)
  An array containing the receiver’s content objects arranged using [`arrange(_:)`](./arrange%28_%29.md).
- [func rearrangeObjects()](./rearrangeobjects%28%29.md)
  Triggers filtering of the receiver’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/arrange(_:))*