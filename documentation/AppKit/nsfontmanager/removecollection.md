# removeCollection(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified font collection.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func removeCollection(_ collectionName: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the font collection was successfully removed; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `collectionName`: The collection to remove.

## See Also

- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](nsfontmanager/availablefontnames(matching:).md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func fontDescriptors(inCollection: String) -> [Any]?](nsfontmanager/fontdescriptors(incollection:).md)
  Returns an array of the font descriptors in the specified collection.
- [func addCollection(String, options: NSFontCollectionOptions) -> Bool](nsfontmanager/addcollection(_:options:).md)
  Adds a specified font collection to the font manager with a given set of options.
- [func addFontDescriptors([Any], toCollection: String)](nsfontmanager/addfontdescriptors(_:tocollection:).md)
  Adds an array of font descriptors to the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](nsfontmanager/removefontdescriptor(_:fromcollection:).md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool](../ObjectiveC/NSObject-swift.class/fontManager(_:willIncludeFont:).md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/removecollection(_:))*