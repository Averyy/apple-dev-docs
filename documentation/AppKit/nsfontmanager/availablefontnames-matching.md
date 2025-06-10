# availableFontNames(matching:)

**Framework**: AppKit  
**Kind**: method

Returns the names of the fonts that match the attributes in the given font descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func availableFontNames(matching descriptor: NSFontDescriptor) -> [Any]?
```

#### Return Value

The names of the matching fonts.

## Parameters

- `descriptor`: The font descriptor whose attributes are matched.

## See Also

- [func fontDescriptors(inCollection: String) -> [Any]?](nsfontmanager/fontdescriptors(incollection:).md)
  Returns an array of the font descriptors in the specified collection.
- [func addCollection(String, options: NSFontCollectionOptions) -> Bool](nsfontmanager/addcollection(_:options:).md)
  Adds a specified font collection to the font manager with a given set of options.
- [func removeCollection(String) -> Bool](nsfontmanager/removecollection(_:).md)
  Removes the specified font collection.
- [func addFontDescriptors([Any], toCollection: String)](nsfontmanager/addfontdescriptors(_:tocollection:).md)
  Adds an array of font descriptors to the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](nsfontmanager/removefontdescriptor(_:fromcollection:).md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool](../ObjectiveC/NSObject-swift.class/fontManager(_:willIncludeFont:).md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/availablefontnames(matching:))*