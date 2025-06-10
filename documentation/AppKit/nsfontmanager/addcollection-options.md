# addCollection(_:options:)

**Framework**: AppKit  
**Kind**: method

Adds a specified font collection to the font manager with a given set of options.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func addCollection(_ collectionName: String, options collectionOptions: NSFontCollectionOptions = []) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the font collection was successfully added; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `collectionName`: The collection to add.
- `collectionOptions`: The option described in  . This option is not yet implemented.

## See Also

- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](nsfontmanager/availablefontnames(matching:).md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func fontDescriptors(inCollection: String) -> [Any]?](nsfontmanager/fontdescriptors(incollection:).md)
  Returns an array of the font descriptors in the specified collection.
- [func removeCollection(String) -> Bool](nsfontmanager/removecollection(_:).md)
  Removes the specified font collection.
- [func addFontDescriptors([Any], toCollection: String)](nsfontmanager/addfontdescriptors(_:tocollection:).md)
  Adds an array of font descriptors to the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](nsfontmanager/removefontdescriptor(_:fromcollection:).md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool](../ObjectiveC/NSObject-swift.class/fontManager(_:willIncludeFont:).md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/addcollection(_:options:))*