# newItem(forRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Returns the collection view item that is used for the specified object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func newItem(forRepresentedObject object: Any) -> NSCollectionViewItem
```

#### Return Value

An initialized collection view item with the specified object and the appropriate view set. The collection view item should not be autoreleased.

#### Discussion

Whenever possible, register classes or nib files for your items instead of using this property. For more information, see Creating Collection View Items.

Subclasses can override this method if the collection view items are not generated from a prototype or if the prototype view needs to be modified. The subclass is responsible for setting the `view`  and representedObject of the new collection view item.

## Parameters

- `object`: The content object that the collection view item will represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/newitem(forrepresentedobject:))*