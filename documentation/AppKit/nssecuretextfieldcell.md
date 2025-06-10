# NSSecureTextFieldCell

**Framework**: AppKit  
**Kind**: class

A text field whose value is hidden from the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTextFieldCell](nstextfieldcell.md)
  An object that enhances the text display capabilities of a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssecuretextfieldcell)*