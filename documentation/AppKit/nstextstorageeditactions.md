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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorageeditactions)*