# NSTextStorageEditActions

**Framework**: AppKit  
**Kind**: struct

Constants that indicate the types of changes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct NSTextStorageEditActions
```

#### Overview

These values are also OR’ed together in notifications to inform instances of `NSLayoutManager` was changed—see [`textStorage(_:edited:range:changeInLength:invalidatedRange:)`](nslayoutmanager/textstorage(_:edited:range:changeinlength:invalidatedrange:).md).

## Topics

### Constants
- [static var editedAttributes: NSTextStorageEditActions](nstextstorageeditactions/editedattributes.md)
  Attributes were added, removed, or changed.
- [static var editedCharacters: NSTextStorageEditActions](nstextstorageeditactions/editedcharacters.md)
  Characters were added, removed, or replaced.
### Initializers
- [init(rawValue: UInt)](nstextstorageeditactions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorageeditactions)*