# UICellAccessory

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An accessory in a collection view list cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UICellAccessory : NSObject
```

## Overview

A cell accessory is a visual element that you can add to a list cell ([`UICollectionViewListCell`](./uicollectionviewlistcell.md)). You use a cell accessory as a visual indicator or to let a user perform a cell-specific action like selecting, reordering, or deleting the cell. A cell accessory appears either on the leading or the trailing edge of a cell, outside of the cell’s content view.

UIKit defines a set of standard system cell accessories. System accessories have default system-defined appearances, but you can make some customizations to them, like setting a custom tint color. You can’t customize the placement of system accessories. If you want additional customization, you can create a custom accessory with [`UICellAccessoryCustomView`](./uicellaccessorycustomview.md).

You add accessories to a list cell by setting its [`accessories`](./uicollectionviewlistcell/accessories-88j0f.md) array.

```objc
UICellAccessoryDisclosureIndicator *disclosure = [[UICellAccessoryDisclosureIndicator alloc] init];
[disclosure setTintColor:[UIColor systemGrayColor]];

[cell setAccessories: @[ [[UICellAccessoryCheckmark alloc] init],
                         disclosure,
                         [[UICellAccessoryDelete alloc] init],
                         [[UICellAccessoryReorder alloc] init]
                      ]];
```

> ❗ **Important**:  The system throws an exception if you include more than one instance of any system accessory. You can include multiple custom accessories.

## Topics

### Creating a cell accessory
- [- init](./uicellaccessory-c.class/init.md)
  Creates a cell accessory object.
- [- initWithCoder:](./uicellaccessory-c.class/initwithcoder_.md)
  Creates a cell accessory object from data in a given unarchiver.
### Creating a system accessory
- [UICellAccessoryDisclosureIndicator](./uicellaccessorydisclosureindicator.md)
  The disclosure indicator system accessory.
- [UICellAccessoryOutlineDisclosure](./uicellaccessoryoutlinedisclosure.md)
  The outline disclosure system accessory.
- [UICellAccessoryPopUpMenu](./uicellaccessorypopupmenu.md)
  The popup menu system accessory.
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
### Creating a custom accessory
- [UICellAccessoryCustomView](./uicellaccessorycustomview.md)
  A custom cell accessory.
### Customizing appearance
- [hidden](./uicellaccessory-c.class/hidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [tintColor](./uicellaccessory-c.class/tintcolor.md)
  The tint color to apply to the accessory.
- [displayedState](./uicellaccessory-c.class/displayedstate.md)
  The cell-editing states that the accessory appears in.
- [UICellAccessoryDisplayedState](./uicellaccessorydisplayedstate.md)
  Constants that describe the cell-editing states that the accessory appears in.
### Customizing layout and placement
- [reservedLayoutWidth](./uicellaccessory-c.class/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory and then centers the accessory within.
- [UICellAccessoryStandardDimension](./uicellaccessorystandarddimension.md)
  The system standard layout dimension for accessories.
- [UICellAccessoryPlacement](./uicellaccessoryplacement.md)
  Constants that describe the placement of the accessory within the cell.
- [UICellAccessoryPosition](./uicellaccessoryposition.md)
  The index position of the cell accessory in relation to the other accessories in the specified array.
- [UICellAccessoryPositionAfterAccessoryOfClass](./uicellaccessorypositionafteraccessoryofclass.md)
  Provides a position after the accessory that matches the specified class, or at the end if there’s no matching class.
- [UICellAccessoryPositionBeforeAccessoryOfClass](./uicellaccessorypositionbeforeaccessoryofclass.md)
  Provides a position before the accessory that matches the specified class, or at the beginning if there’s no matching class.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UICellAccessoryCheckmark](./uicellaccessorycheckmark.md)
- [UICellAccessoryCustomView](./uicellaccessorycustomview.md)
- [UICellAccessoryDelete](./uicellaccessorydelete.md)
- [UICellAccessoryDetail](./uicellaccessorydetail.md)
- [UICellAccessoryDisclosureIndicator](./uicellaccessorydisclosureindicator.md)
- [UICellAccessoryInsert](./uicellaccessoryinsert.md)
- [UICellAccessoryLabel](./uicellaccessorylabel.md)
- [UICellAccessoryMultiselect](./uicellaccessorymultiselect.md)
- [UICellAccessoryOutlineDisclosure](./uicellaccessoryoutlinedisclosure.md)
- [UICellAccessoryPopUpMenu](./uicellaccessorypopupmenu.md)
- [UICellAccessoryReorder](./uicellaccessoryreorder.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Managing cell accessories
- [accessories](./uicollectionviewlistcell/accessories-88j0f.md)
  An array of the accessories that decorate the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-c.class)*