# NSFontCollectionOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that support font collection management.

**Availability**:
- macOS

## Declaration

```swift
struct NSFontCollectionOptions
```

```c
enum NSFontCollectionOptions : NSUInteger;
```

## Topics

### Options
- [static var applicationOnlyMask: NSFontCollectionOptions](./nsfontcollectionoptions/applicationonlymask.md)
  Makes the collection available only to the application.
### Initializers
- [init(rawValue: UInt)](./nsfontcollectionoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Management
- [class NSFontManager](./nsfontmanager.md)
  The center of activity for the font-conversion system.
- [class NSFontCollection](./nsfontcollection.md)
  A font collection, which is a group of font descriptors taken together as a single object.
- [class NSMutableFontCollection](./nsmutablefontcollection.md)
  A mutable collection of font descriptors taken together as a single object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollectionoptions)*