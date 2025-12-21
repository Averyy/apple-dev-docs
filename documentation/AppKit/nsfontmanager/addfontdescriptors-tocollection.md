# addFontDescriptors(_:toCollection:)

**Framework**: AppKit  
**Kind**: method

Adds an array of font descriptors to the specified font collection.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func addFontDescriptors(_ descriptors: [Any], toCollection collectionName: String)
```

## Parameters

- `descriptors`: The font descriptors to add.
- `collectionName`: The font collection to which descriptors are added.

## See Also

- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](nsfontmanager/availablefontnames(matching:).md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func fontDescriptors(inCollection: String) -> [Any]?](nsfontmanager/fontdescriptors(incollection:).md)
  Returns an array of the font descriptors in the specified collection.
- [func addCollection(String, options: NSFontCollectionOptions) -> Bool](nsfontmanager/addcollection(_:options:).md)
  Adds a specified font collection to the font manager with a given set of options.
- [func removeCollection(String) -> Bool](nsfontmanager/removecollection(_:).md)
  Removes the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](nsfontmanager/removefontdescriptor(_:fromcollection:).md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(Any, willIncludeFont: String) -> Bool](../ObjectiveC/NSObject-swift.class/fontManager(_:willIncludeFont:).md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/addfontdescriptors(_:tocollection:))*