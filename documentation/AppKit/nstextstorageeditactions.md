# NSTextStorageEditActions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate the types of changes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct NSTextStorageEditActions
```

```c
enum NSTextStorageEditActions : NSUInteger;
```

## Overview

These values are also OR’ed together in notifications to inform instances of `NSLayoutManager` was changed—see [`textStorage(_:edited:range:changeInLength:invalidatedRange:)`](./nslayoutmanager/textstorage%28_,edited,range,changeinlength,invalidatedrange%29.md).

## Topics

### Constants
- [static var editedAttributes: NSTextStorageEditActions](./nstextstorageeditactions/editedattributes.md)
  Attributes were added, removed, or changed.
- [static var editedCharacters: NSTextStorageEditActions](./nstextstorageeditactions/editedcharacters.md)
  Characters were added, removed, or replaced.
### Initializers
- [init(rawValue: UInt)](./nstextstorageeditactions/init%28rawvalue%29.md)

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

### Constants
- [NSTextStorageEditedOptions](./nstextstorageeditedoptions.md)
  ** Deprecations ***


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorageeditactions)*