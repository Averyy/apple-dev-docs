# NSFontCollection.Name

**Framework**: AppKit  
**Kind**: struct

The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](nsfontcollection/allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Name
```

## Topics

### Type Properties
- [static let allFonts: NSFontCollection.Name](nsfontcollection/name/allfonts.md)
  All fonts in the system.
- [static let user: NSFontCollection.Name](nsfontcollection/name/user.md)
  Per-user unmodifiable collection.
- [static let favorites: NSFontCollection.Name](nsfontcollection/name/favorites.md)
  Font collection of the user’s preferred font descriptors.
- [static let recentlyUsed: NSFontCollection.Name](nsfontcollection/name/recentlyused.md)
  Font collection automatically maintained by NSFontManager.
### Initializers
- [init(String)](nsfontcollection/name/init(_:).md)
- [init(rawValue: String)](nsfontcollection/name/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func rename(fromName: NSFontCollection.Name, visibility: NSFontCollection.Visibility, toName: NSFontCollection.Name) throws](nsfontcollection/rename(fromname:visibility:toname:).md)
  Renames the font collection with the specified name and visibility to the second name specified.
- [class func show(NSFontCollection, withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](nsfontcollection/show(_:withname:visibility:).md)
  Make the given font collection visible by giving it a name.
- [class func hide(withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](nsfontcollection/hide(withname:visibility:).md)
  Remove from view the named font collection with the specified visibility.
- [class var allFontCollectionNames: [NSFontCollection.Name]](nsfontcollection/allfontcollectionnames.md)
  Returns all named collections visible to this process.
- [NSFontCollection.Visibility](nsfontcollection/visibility.md)
  Constants that specify the visibility of font collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/name)*