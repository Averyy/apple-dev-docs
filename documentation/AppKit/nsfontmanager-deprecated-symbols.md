# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](./nsfontmanager/availablefontnames%28matching%29.md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func fontDescriptors(inCollection: String) -> [Any]?](./nsfontmanager/fontdescriptors%28incollection%29.md)
  Returns an array of the font descriptors in the specified collection.
- [func addCollection(String, options: NSFontCollectionOptions) -> Bool](./nsfontmanager/addcollection%28_,options%29.md)
  Adds a specified font collection to the font manager with a given set of options.
- [func removeCollection(String) -> Bool](./nsfontmanager/removecollection%28_%29.md)
  Removes the specified font collection.
- [func addFontDescriptors([Any], toCollection: String)](./nsfontmanager/addfontdescriptors%28_,tocollection%29.md)
  Adds an array of font descriptors to the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](./nsfontmanager/removefontdescriptor%28_,fromcollection%29.md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(Any, willIncludeFont: String) -> Bool](../ObjectiveC/nsobject-swift.class/fontmanager%28_,willincludefont%29.md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.
### Deprecated properties
- [static var applicationOnlyMask: NSFontCollectionOptions](./nsfontcollectionoptions/applicationonlymask.md)
  Makes the collection available only to the application.
- [var collectionNames: [Any]](./nsfontmanager/collectionnames.md)
  The names of the currently loaded font collections.
- [var delegate: AnyObject?](./nsfontmanager/delegate.md)
  The font manager’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager-deprecated-symbols)*