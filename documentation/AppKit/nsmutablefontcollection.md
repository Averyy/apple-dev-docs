# NSMutableFontCollection

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A mutable collection of font descriptors taken together as a single object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSMutableFontCollection
```

```objc
@interface NSMutableFontCollection : NSFontCollection
```

#### Overview

You can use this class to modify the search queries for the font descriptors used by the parent [`NSFontCollection`](./nsfontcollection.md) class.

## Topics

### Creating a Font Collection
- [init(descriptors: [NSFontDescriptor])](./nsmutablefontcollection/init%28descriptors%29.md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init(locale: Locale)](./nsmutablefontcollection/init%28locale%29.md)
  Creates a mutable font collection containing fonts suitable for the specified locale.
- [init?(name: NSFontCollection.Name)](./nsmutablefontcollection/init%28name%29.md)
  Creates a mutable named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./nsmutablefontcollection/init%28name,visibility%29.md)
  Creates a mutable font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSMutableFontCollection](./nsmutablefontcollection/withallavailabledescriptors.md)
  The mutable font collection that matches all registered fonts.
### Getting the Font Descriptors
- [var queryDescriptors: [NSFontDescriptor]?](./nsmutablefontcollection/querydescriptors.md)
  The font descriptors to include in query results.
- [func addQuery(for: [NSFontDescriptor])](./nsmutablefontcollection/addquery%28for%29.md)
  Edits the query and exclusion arrays by adding the specified font descriptors.
- [func removeQuery(for: [NSFontDescriptor])](./nsmutablefontcollection/removequery%28for%29.md)
  Edits the query and exclusion arrays by removing the specified font descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](./nsmutablefontcollection/exclusiondescriptors.md)
  The font descriptors to exclude from query results.

## Relationships

### Inherits From
- [NSFontCollection](./nsfontcollection.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Management
- [class NSFontManager](./nsfontmanager.md)
  The center of activity for the font-conversion system.
- [class NSFontCollection](./nsfontcollection.md)
  A font collection, which is a group of font descriptors taken together as a single object.
- [struct NSFontCollectionOptions](./nsfontcollectionoptions.md)
  Constants that support font collection management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection)*