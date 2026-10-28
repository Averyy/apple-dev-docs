# allFontCollectionNames

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns all named collections visible to this process.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class var allFontCollectionNames: [NSFontCollection.Name] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * allFontCollectionNames;
```

## Return Value

`NSString` objects containing the names of all the named collections.

## See Also

### Naming the Font Collection
- [class func rename(fromName: NSFontCollection.Name, visibility: NSFontCollection.Visibility, toName: NSFontCollection.Name) throws](./rename%28fromname,visibility,toname%29.md)
  Renames the font collection with the specified name and visibility to the second name specified.
- [class func show(NSFontCollection, withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](./show%28_,withname,visibility%29.md)
  Make the given font collection visible by giving it a name.
- [class func hide(withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](./hide%28withname,visibility%29.md)
  Remove from view the named font collection with the specified visibility.
- [NSFontCollection.Name](./name.md)
  The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](./allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.
- [NSFontCollection.Visibility](./visibility.md)
  Constants that specify the visibility of font collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/allfontcollectionnames)*