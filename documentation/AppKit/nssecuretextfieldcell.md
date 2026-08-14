# NSSecureTextFieldCell

**Framework**: AppKit  
**Kind**: class

A text field whose value is hidden from the user.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSSecureTextFieldCell
```

#### Overview

[`NSSecureTextFieldCell`](nssecuretextfieldcell.md) works with [`NSSecureTextField`](nssecuretextfield.md) and overrides the general cell use of the field editor to provide its own field editor, which doesn’t display text or allow the user to cut or copy its value.

## Topics

### Working with character echo
- [var echosBullets: Bool](nssecuretextfieldcell/echosbullets.md)
  A Boolean that indicates whether the receiver echoes a bullet character rather than each character typed.

## Relationships

### Inherits From
- [NSTextFieldCell](nstextfieldcell.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NSTextFieldCell](nstextfieldcell.md)
  An object that enhances the text display capabilities of a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssecuretextfieldcell)*