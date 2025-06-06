# Deprecated Symbols

**Framework**: AppKit

Review unsupported symbols and their replacements.

## Topics

### Methods
- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](nsfontmanager/availablefontnames(matching:).md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
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
### Properties
- [static var applicationOnlyMask: NSFontCollectionOptions](nsfontcollectionoptions/applicationonlymask.md)
  Makes the collection available only to the application.
- [var collectionNames: [Any]](nsfontmanager/collectionnames.md)
  The names of the currently loaded font collections.
- [var delegate: AnyObject?](nsfontmanager/delegate.md)
  The font manager’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager-deprecated-symbols)*