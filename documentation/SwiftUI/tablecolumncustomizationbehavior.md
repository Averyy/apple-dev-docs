# TableColumnCustomizationBehavior

**Framework**: SwiftUI  
**Kind**: struct

A set of customization behaviors of a column that a table can offer to a user.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct TableColumnCustomizationBehavior
```

#### Overview

This is used as a value provided to [`disabledCustomizationBehavior(_:)`](tablecolumncontent/disabledcustomizationbehavior(_:).md).

Setting any of these values as the `disabledCustomizationBehavior(_:)` doesn’t have any effect on iOS.

## Topics

### Getting the customization behavior
- [static var all: TableColumnCustomizationBehavior](tablecolumncustomizationbehavior/all.md)
  All customization behaviors.
- [static let reorder: TableColumnCustomizationBehavior](tablecolumncustomizationbehavior/reorder.md)
  A behavior that allows the column to be reordered by the user.
- [static let resize: TableColumnCustomizationBehavior](tablecolumncustomizationbehavior/resize.md)
  A behavior that allows the column to be resized by the user.
- [static let visibility: TableColumnCustomizationBehavior](tablecolumncustomizationbehavior/visibility.md)
  A behavior that allows the column to be hidden or revealed by the user.
### Creating a behavior
- [init()](tablecolumncustomizationbehavior/init.md)
  Creates an empty customization behavior, representing no customization

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func tableColumnHeaders(Visibility) -> some View](view/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [struct TableColumnCustomization](tablecolumncustomization.md)
  A representation of the state of the columns in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncustomizationbehavior)*