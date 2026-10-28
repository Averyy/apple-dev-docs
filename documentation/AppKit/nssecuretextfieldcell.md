# NSSecureTextFieldCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A text field whose value is hidden from the user.

**Availability**:
- macOS

## Declaration

```swift
class NSSecureTextFieldCell
```

```objc
@interface NSSecureTextFieldCell : NSTextFieldCell
```

## Overview

[`NSSecureTextFieldCell`](./nssecuretextfieldcell.md) works with [`NSSecureTextField`](./nssecuretextfield.md) and overrides the general cell use of the field editor to provide its own field editor, which doesn’t display text or allow the user to cut or copy its value.

## Topics

### Working with character echo
- [var echosBullets: Bool](./nssecuretextfieldcell/echosbullets.md)
  A Boolean that indicates whether the receiver echoes a bullet character rather than each character typed.

## Relationships

### Inherits From
- [NSTextFieldCell](./nstextfieldcell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Cell
- [class NSTextFieldCell](./nstextfieldcell.md)
  An object that enhances the text display capabilities of a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssecuretextfieldcell)*