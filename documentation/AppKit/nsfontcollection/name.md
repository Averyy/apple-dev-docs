# NSFontCollection.Name

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](./allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.

**Availability**:
- macOS

## Declaration

```swift
struct Name
```

```c
typedef NSString * NSFontCollectionName;
```

## Topics

### Type Properties
- [static let allFonts: NSFontCollection.Name](./name/allfonts.md)
  All fonts in the system.
- [static let user: NSFontCollection.Name](./name/user.md)
  Per-user unmodifiable collection.
- [static let favorites: NSFontCollection.Name](./name/favorites.md)
  Font collection of the user’s preferred font descriptors.
- [static let recentlyUsed: NSFontCollection.Name](./name/recentlyused.md)
  Font collection automatically maintained by NSFontManager.
### Initializers
- [init(String)](./name/init%28_%29.md)
- [init(rawValue: String)](./name/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Naming the Font Collection
- [class func rename(fromName: NSFontCollection.Name, visibility: NSFontCollection.Visibility, toName: NSFontCollection.Name) throws](./rename%28fromname,visibility,toname%29.md)
  Renames the font collection with the specified name and visibility to the second name specified.
- [class func show(NSFontCollection, withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](./show%28_,withname,visibility%29.md)
  Make the given font collection visible by giving it a name.
- [class func hide(withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](./hide%28withname,visibility%29.md)
  Remove from view the named font collection with the specified visibility.
- [class var allFontCollectionNames: [NSFontCollection.Name]](./allfontcollectionnames.md)
  Returns all named collections visible to this process.
- [NSFontCollection.Visibility](./visibility.md)
  Constants that specify the visibility of font collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/name)*