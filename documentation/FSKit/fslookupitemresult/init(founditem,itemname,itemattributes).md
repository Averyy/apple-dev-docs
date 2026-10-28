# init(foundItem:itemName:itemAttributes:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a result for an item-lookup operation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(foundItem: FSItem, itemName: FSFileName, itemAttributes: FSItem.Attributes)
```

```objc
- (instancetype) initWithFoundItem:(FSItem *) foundItem itemName:(FSFileName *) itemName itemAttributes:(FSItemAttributes *) itemAttributes;
```

## Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `foundItem`: The [`FSItem`](../fsitem.md) found by the directory lookup.
- `itemName`: The item’s name as it exists within the file system. The value may differ from the requested name in order to handle case-insensitive file systems or Unicode normalization.
- `itemAttributes`: The [`FSItem.Attributes`](../fsitem/attributes.md) of the found item.

## See Also

### Creating a lookup item result
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSFileName](../fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](../fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fslookupitemresult/init(founditem:itemname:itemattributes:))*