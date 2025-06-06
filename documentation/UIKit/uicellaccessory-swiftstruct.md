# UICellAccessory

**Framework**: UIKit  
**Kind**: struct

An accessory in a collection view list cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct UICellAccessory
```

#### Overview

A cell accessory is a visual element that you can add to a list cell ([`UICollectionViewListCell`](uicollectionviewlistcell.md)). You use a cell accessory as a visual indicator or to let a user perform a cell-specific action like selecting, reordering, or deleting the cell. A cell accessory appears either on the leading or the trailing edge of a cell, outside of the cell’s content view.

UIKit defines a set of standard system cell accessories. System accessories have default system-defined appearances, but you can make some customizations to them, like setting a custom tint color. You can’t customize the placement of system accessories. If you want additional customization, you can create a custom accessory with [`customView(configuration:)`](uicellaccessory-swift.struct/customview(configuration:).md).

You add accessories to a list cell by setting its [`accessories`](uicollectionviewlistcell/accessories-88j0f.md) array.

```swift
cell.accessories = [ 
    .checkmark(), 
    .disclosureIndicator(options: .init(tintColor: .systemGray)), 
    .delete(),
    .reorder() 
]
```

> ❗ **Important**:  The system throws an exception if you include more than one instance of any system accessory. You can include multiple custom accessories.

 The system throws an exception if you include more than one instance of any system accessory. You can include multiple custom accessories.

## Topics

### Creating a disclosure indicator
- [static func disclosureIndicator(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.DisclosureIndicatorOptions) -> UICellAccessory](uicellaccessory-swift.struct/disclosureindicator(displayed:options:).md)
  Creates a disclosure indicator system accessory with the specified display state and configuration options.
- [UICellAccessory.DisclosureIndicatorOptions](uicellaccessory-swift.struct/disclosureindicatoroptions.md)
  Configuration options for a disclosure indicator.
### Creating an outline disclosure
- [static func outlineDisclosure(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.OutlineDisclosureOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](uicellaccessory-swift.struct/outlinedisclosure(displayed:options:actionhandler:).md)
  Creates an outline disclosure system accessory with the specified display state, configuration options, and optional action handler.
- [UICellAccessory.OutlineDisclosureOptions](uicellaccessory-swift.struct/outlinedisclosureoptions.md)
  Configuration options for an outline disclosure.
### Creating a popup menu accessory
- [static func popUpMenu(UIMenu, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.PopUpMenuOptions, selectedElementDidChangeHandler: UICellAccessory.MenuSelectedElementDidChangeHandler?) -> UICellAccessory](uicellaccessory-swift.struct/popupmenu(_:displayed:options:selectedelementdidchangehandler:).md)
  Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.
- [UICellAccessory.MenuSelectedElementDidChangeHandler](uicellaccessory-swift.struct/menuselectedelementdidchangehandler.md)
  A closure type that defines a handler to perform when a user selects an element in the menu.
- [UICellAccessory.PopUpMenuOptions](uicellaccessory-swift.struct/popupmenuoptions.md)
  Configuration options for a popup menu accessory.
### Creating a checkmark accessory
- [static func checkmark(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.CheckmarkOptions) -> UICellAccessory](uicellaccessory-swift.struct/checkmark(displayed:options:).md)
  Creates a checkmark system accessory with the specified display state and configuration options.
- [UICellAccessory.CheckmarkOptions](uicellaccessory-swift.struct/checkmarkoptions.md)
  Configuration options for a checkmark accessory.
### Creating a delete accessory
- [static func delete(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.DeleteOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](uicellaccessory-swift.struct/delete(displayed:options:actionhandler:).md)
  Creates a delete system accessory with the specified display state, configuration options, and optional action handler.
- [UICellAccessory.DeleteOptions](uicellaccessory-swift.struct/deleteoptions.md)
  Configuration options for a delete accessory.
### Creating an insert accessory
- [static func insert(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.InsertOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](uicellaccessory-swift.struct/insert(displayed:options:actionhandler:).md)
  Creates an insert system accessory with the specified display state, configuration options, and optional action handler.
- [UICellAccessory.InsertOptions](uicellaccessory-swift.struct/insertoptions.md)
  Configuration options for an insert accessory.
### Creating a reorder accessory
- [static func reorder(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.ReorderOptions) -> UICellAccessory](uicellaccessory-swift.struct/reorder(displayed:options:).md)
  Creates a reorder system accessory with the specified display state and configuration options.
- [UICellAccessory.ReorderOptions](uicellaccessory-swift.struct/reorderoptions.md)
  Configuration options for a reorder accessory.
### Creating a multiselect accessory
- [static func multiselect(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.MultiselectOptions) -> UICellAccessory](uicellaccessory-swift.struct/multiselect(displayed:options:).md)
  Creates a multiselect system accessory with the specified display state and configuration options.
- [UICellAccessory.MultiselectOptions](uicellaccessory-swift.struct/multiselectoptions.md)
  Configuration options for a multiselect accessory.
### Creating a label accessory
- [static func label(text: String, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.LabelOptions) -> UICellAccessory](uicellaccessory-swift.struct/label(text:displayed:options:).md)
  Creates a label system accessory with the specified text, display state, and configuration options.
- [UICellAccessory.LabelOptions](uicellaccessory-swift.struct/labeloptions.md)
  Configuration options for a label accessory.
### Creating a detail accessory
- [static func detail(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.DetailOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](uicellaccessory-swift.struct/detail(displayed:options:actionhandler:).md)
  Creates a detail system accessory with the specified display state, configuration options, and optional action handler.
- [UICellAccessory.DetailOptions](uicellaccessory-swift.struct/detailoptions.md)
  Configuration options for a detail accessory.
### Creating a custom accessory
- [static func customView(configuration: UICellAccessory.CustomViewConfiguration) -> UICellAccessory](uicellaccessory-swift.struct/customview(configuration:).md)
  Creates a custom view accessory.
- [UICellAccessory.CustomViewConfiguration](uicellaccessory-swift.struct/customviewconfiguration.md)
  Configuration options for a custom accessory.
### Checking the accessory’s type
- [let accessoryType: UICellAccessory.AccessoryType](uicellaccessory-swift.struct/accessorytype-swift.property.md)
  The type of the cell accessory.
- [UICellAccessory.AccessoryType](uicellaccessory-swift.struct/accessorytype-swift.enum.md)
  Constants that describe the type of the cell accessory.
### Customizing appearance and placement
- [UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/layoutdimension.md)
  Constants that describe the layout dimension for the accessory.
- [UICellAccessory.Placement](uicellaccessory-swift.struct/placement.md)
  Constants that describe the placement of the accessory within the cell.
- [UICellAccessory.DisplayedState](uicellaccessory-swift.struct/displayedstate.md)
  Constants that describe the cell-editing states that the accessory appears in.
### Performing accessory actions
- [UICellAccessory.ActionHandler](uicellaccessory-swift.struct/actionhandler.md)
  A closure that the system calls when a user taps a cell accessory.

## See Also

- [var accessories: [UICellAccessory]](uicollectionviewlistcell/accessories-8nui4.md)
  An array of the accessories that decorate the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct)*