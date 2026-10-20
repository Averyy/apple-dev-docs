# UIAccessibilityContainerType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the type of content in a data-based container.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum UIAccessibilityContainerType
```

```c
enum UIAccessibilityContainerType : NSInteger;
```

## Topics

### Constants
- [UIAccessibilityContainerType.none](./uiaccessibilitycontainertype/none.md)
  No additional data.
- [UIAccessibilityContainerType.dataTable](./uiaccessibilitycontainertype/datatable.md)
  A table that contains structured data.
- [UIAccessibilityContainerType.list](./uiaccessibilitycontainertype/list.md)
  A list of data.
- [UIAccessibilityContainerType.landmark](./uiaccessibilitycontainertype/landmark.md)
  Landmark data.
- [UIAccessibilityContainerType.semanticGroup](./uiaccessibilitycontainertype/semanticgroup.md)
  A semantic group of data.
### Useful links
- [Accessibility design for Mac Catalyst](../Accessibility/accessibility_design_for_mac_catalyst.md)
  Improve navigation in your app by using keyboard shortcuts and accessibility containers.
### Initializers
- [init?(rawValue: Int)](./uiaccessibilitycontainertype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Containers
- [protocol UIAccessibilityContainerDataTable](./uiaccessibilitycontainerdatatable.md)
  Methods that convey information about the contents of a table.
- [protocol UIAccessibilityContainerDataTableCell](./uiaccessibilitycontainerdatatablecell.md)
  Methods that provide the location of a cell in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainertype)*