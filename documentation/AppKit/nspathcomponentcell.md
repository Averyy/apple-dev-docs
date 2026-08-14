# NSPathComponentCell

**Framework**: AppKit  
**Kind**: class

A component of a path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSPathComponentCell
```

#### Overview

An `NSPathCell` object manages a collection of `NSPathComponentCell` objects, in conjunction with an `NSPathControl` object, to represent a path.

## Topics

### Setting the Image
- [var image: NSImage?](nspathcomponentcell/image.md)
  The image displayed for this component cell.
### Setting the Path
- [var url: URL?](nspathcomponentcell/url.md)
  The portion of the path from the root through the component represented by the receiver.

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

- [class NSPathCell](nspathcell.md)
  The user interface of a path control object.
- [protocol NSPathCellDelegate](nspathcelldelegate.md)
  A set of methods that enable the delegate of a path cell object to customize the Open panel or pop-up menu of a path whose style is set to [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md).
- [class NSPathControlItem](nspathcontrolitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcomponentcell)*