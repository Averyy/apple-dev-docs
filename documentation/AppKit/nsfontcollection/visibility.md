# NSFontCollection.Visibility

**Framework**: AppKit  
**Kind**: struct

Constants that specify the visibility of font collections.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Visibility
```

## Topics

### Visibility Options
- [static var process: NSFontCollection.Visibility](nsfontcollection/visibility/process.md)
  The font collection is visible within this process and is not persistent.
- [static var user: NSFontCollection.Visibility](nsfontcollection/visibility/user.md)
  The font collection is visible to all processes and is stored persistently.
- [static var computer: NSFontCollection.Visibility](nsfontcollection/visibility/computer.md)
  The font collection is visible to all users and is stored persistently.
### Initializers
- [init(rawValue: UInt)](nsfontcollection/visibility/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func rename(fromName: NSFontCollection.Name, visibility: NSFontCollection.Visibility, toName: NSFontCollection.Name) throws](nsfontcollection/rename(fromname:visibility:toname:).md)
  Renames the font collection with the specified name and visibility to the second name specified.
- [class func show(NSFontCollection, withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](nsfontcollection/show(_:withname:visibility:).md)
  Make the given font collection visible by giving it a name.
- [class func hide(withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](nsfontcollection/hide(withname:visibility:).md)
  Remove from view the named font collection with the specified visibility.
- [class var allFontCollectionNames: [NSFontCollection.Name]](nsfontcollection/allfontcollectionnames.md)
  Returns all named collections visible to this process.
- [NSFontCollection.Name](nsfontcollection/name.md)
  The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](nsfontcollection/allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/visibility)*