# UICellAccessoryPopUpMenu

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The popup menu system accessory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@interface UICellAccessoryPopUpMenu : UICellAccessory
```

#### Overview

A popup menu accessory is a pair of chevrons that point upward and downward. This accessory indicates that tapping anywhere in the cell presents a popup menu. This accessory appears on the trailing edge of the cell.

## Topics

### Creating configuration options
- [- initWithMenu:](./uicellaccessorypopupmenu/initwithmenu_.md)
  Creates a popup menu accessory with the specified menu.
- [- initWithCoder:](./uicellaccessorypopupmenu/initwithcoder_.md)
  Creates a popup menu accessory from data in an unarchiver.
### Accessing configuration options
- [menu](./uicellaccessorypopupmenu/menu.md)
  The menu to display when a user taps the popup menu accessory.
- [selectedElementDidChangeHandler](./uicellaccessorypopupmenu/selectedelementdidchangehandler.md)
  An optional closure that the system calls when a user selects an element in the menu.

## Relationships

### Inherits From
- [UICellAccessory](./uicellaccessory-c.class.md)

## See Also

### Creating a system accessory
- [UICellAccessoryDisclosureIndicator](./uicellaccessorydisclosureindicator.md)
  The disclosure indicator system accessory.
- [UICellAccessoryOutlineDisclosure](./uicellaccessoryoutlinedisclosure.md)
  The outline disclosure system accessory.
- [UICellAccessoryCheckmark](./uicellaccessorycheckmark.md)
  The checkmark system accessory.
- [UICellAccessoryDelete](./uicellaccessorydelete.md)
  The delete system accessory.
- [UICellAccessoryInsert](./uicellaccessoryinsert.md)
  The insert system accessory.
- [UICellAccessoryReorder](./uicellaccessoryreorder.md)
  The reorder system accessory.
- [UICellAccessoryMultiselect](./uicellaccessorymultiselect.md)
  The multiselect system accessory.
- [UICellAccessoryLabel](./uicellaccessorylabel.md)
  The label system accessory.
- [UICellAccessoryDetail](./uicellaccessorydetail.md)
  The detail system accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessorypopupmenu)*