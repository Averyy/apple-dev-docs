# NSMutableFontCollection

**Framework**: AppKit  
**Kind**: class

A mutable collection of font descriptors taken together as a single object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSMutableFontCollection
```

#### Overview

You can use this class to modify the search queries for the font descriptors used by the parent [`NSFontCollection`](nsfontcollection.md) class.

## Topics

### Creating a Font Collection
- [init(descriptors: [NSFontDescriptor])](nsmutablefontcollection/init(descriptors:).md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init(locale: Locale)](nsmutablefontcollection/init(locale:).md)
  Creates a mutable font collection containing fonts suitable for the specified locale.
- [init?(name: NSFontCollection.Name)](nsmutablefontcollection/init(name:).md)
  Creates a mutable named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](nsmutablefontcollection/init(name:visibility:).md)
  Creates a mutable font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSMutableFontCollection](nsmutablefontcollection/withallavailabledescriptors.md)
  The mutable font collection that matches all registered fonts.
### Getting the Font Descriptors
- [var queryDescriptors: [NSFontDescriptor]?](nsmutablefontcollection/querydescriptors.md)
  The font descriptors to include in query results.
- [func addQuery(for: [NSFontDescriptor])](nsmutablefontcollection/addquery(for:).md)
  Edits the query and exclusion arrays by adding the specified font descriptors.
- [func removeQuery(for: [NSFontDescriptor])](nsmutablefontcollection/removequery(for:).md)
  Edits the query and exclusion arrays by removing the specified font descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](nsmutablefontcollection/exclusiondescriptors.md)
  The font descriptors to exclude from query results.

## Relationships

### Inherits From
- [NSFontCollection](nsfontcollection.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSFontManager](nsfontmanager.md)
  The center of activity for the font-conversion system.
- [class NSFontCollection](nsfontcollection.md)
  A font collection, which is a group of font descriptors taken together as a single object.
- [struct NSFontCollectionOptions](nsfontcollectionoptions.md)
  Constants that support font collection management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection)*