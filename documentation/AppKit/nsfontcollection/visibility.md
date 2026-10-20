# NSFontCollection.Visibility

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the visibility of font collections.

**Availability**:
- macOS

## Declaration

```swift
struct Visibility
```

```c
enum NSFontCollectionVisibility : NSUInteger;
```

## Topics

### Visibility Options
- [static var process: NSFontCollection.Visibility](./visibility/process.md)
  The font collection is visible within this process and is not persistent.
- [static var user: NSFontCollection.Visibility](./visibility/user.md)
  The font collection is visible to all processes and is stored persistently.
- [static var computer: NSFontCollection.Visibility](./visibility/computer.md)
  The font collection is visible to all users and is stored persistently.
### Initializers
- [init(rawValue: UInt)](./visibility/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

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
- [NSFontCollection.Name](./name.md)
  The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](./allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/visibility)*