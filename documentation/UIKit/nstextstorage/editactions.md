# NSTextStorage.EditActions

**Framework**: UIKit  
**Kind**: struct

Constants that indicate the types of changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct EditActions
```

#### Overview

These values are also OR’ed together in notifications to inform instances of `NSLayoutManager` was changed—see [`textStorage(_:edited:range:changeInLength:invalidatedRange:)`](https://developer.apple.com/documentation/AppKit/NSLayoutManager/textStorage(_:edited:range:changeInLength:invalidatedRange:)).

## Topics

### Constants
- [static var editedAttributes: NSTextStorage.EditActions](nstextstorage/editactions/editedattributes.md)
  Attributes were added, removed, or changed.
- [static var editedCharacters: NSTextStorage.EditActions](nstextstorage/editactions/editedcharacters.md)
  Characters were added, removed, or replaced.
### Initializers
- [init(rawValue: UInt)](nstextstorage/editactions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/editactions)*