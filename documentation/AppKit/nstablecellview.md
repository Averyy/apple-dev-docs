# NSTableCellView

**Framework**: AppKit  
**Kind**: class

A reusable container view shown for a particular cell in a table view that uses rows for content.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class NSTableCellView
```

#### Overview

The [`imageView`](nstablecellview/imageview.md) and [`textField`](nstablecellview/textfield.md) properties are connected in Interface Builder. Additional properties can be added by subclassing [`NSTableCellView`](nstablecellview.md) and adding the required properties and connecting them programmatically or in Interface Builder.

The `objectValue` is used when setting the value of the view cell by the [`tableView(_:objectValueFor:row:)`](nstableviewdatasource/tableview(_:objectvaluefor:row:).md) method in the [`NSTableViewDataSource`](nstableviewdatasource.md). If you use your own custom view cells that are not based on [`NSTableCellView`](nstablecellview.md) you should implement this property in order to be able to receive changes to cell values.

## Topics

### Represented Object
- [var objectValue: Any?](nstablecellview/objectvalue.md)
  The object that represents the cell data.
### Displayed Items
- [var imageView: NSImageView?](nstablecellview/imageview.md)
  Image displayed by the cell.
- [var textField: NSTextField?](nstablecellview/textfield.md)
  Text displayed by the cell.
### Getting and Setting the Background Style
- [var backgroundStyle: NSView.BackgroundStyle](nstablecellview/backgroundstyle.md)
  This property is automatically set by the enclosing row view to let this view know what its background looks like.
### Getting and Setting the Row Size Style
- [var rowSizeStyle: NSTableView.RowSizeStyle](nstablecellview/rowsizestyle.md)
  Returns the row size style.
### Dragging Images
- [var draggingImageComponents: [NSDraggingImageComponent]](nstablecellview/draggingimagecomponents.md)
  Returns dragging images for the cell.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSTableView](nstableview.md)
  A set of related records, displayed in rows that represent individual records and columns that represent the attributes of those records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview)*