# NSPathComponentCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A component of a path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSPathComponentCell
```

```objc
@interface NSPathComponentCell : NSTextFieldCell
```

## Overview

An `NSPathCell` object manages a collection of `NSPathComponentCell` objects, in conjunction with an `NSPathControl` object, to represent a path.

## Topics

### Setting the Image
- [var image: NSImage?](./nspathcomponentcell/image.md)
  The image displayed for this component cell.
### Setting the Path
- [var url: URL?](./nspathcomponentcell/url.md)
  The portion of the path from the root through the component represented by the receiver.

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

### Cells
- [class NSPathCell](./nspathcell.md)
  The user interface of a path control object.
- [protocol NSPathCellDelegate](./nspathcelldelegate.md)
  A set of methods that enable the delegate of a path cell object to customize the Open panel or pop-up menu of a path whose style is set to [`NSPathControl.Style.popUp`](./nspathcontrol/style/popup.md).
- [class NSPathControlItem](./nspathcontrolitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcomponentcell)*