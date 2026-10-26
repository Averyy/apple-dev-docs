# NSTextStorage.EditActions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate the types of changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct EditActions
```

```c
enum NSTextStorageEditActions : NSUInteger;
```

#### Overview

These values are also OR’ed together in notifications to inform instances of `NSLayoutManager` was changed—see [`textStorage(_:edited:range:changeInLength:invalidatedRange:)`](../../AppKit/nslayoutmanager/textstorage%28_,edited,range,changeinlength,invalidatedrange%29.md).

## Topics

### Constants
- [static var editedAttributes: NSTextStorage.EditActions](./editactions/editedattributes.md)
  Attributes were added, removed, or changed.
- [static var editedCharacters: NSTextStorage.EditActions](./editactions/editedcharacters.md)
  Characters were added, removed, or replaced.
### Initializers
- [init(rawValue: UInt)](./editactions/init%28rawvalue%29.md)

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

### Constants
- [NSTextStorageEditedOptions](../../AppKit/nstextstorageeditedoptions.md)
  ** Deprecations ***


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/editactions)*