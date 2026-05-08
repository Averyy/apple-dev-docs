# GroupedFormStyle

**Framework**: SwiftUI  
**Kind**: struct

A form style with grouped rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct GroupedFormStyle
```

#### Overview

Rows in this form style have leading aligned labels and trailing aligned controls within visually grouped sections.

Use the [`grouped`](formstyle/grouped.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.grouped)
```

## Topics

### Creating the form style
- [init()](groupedformstyle/init.md)
  Creates a form style with scrolling, grouped rows.

## Relationships

### Conforms To
- [FormStyle](formstyle.md)

## See Also

- [struct AutomaticFormStyle](automaticformstyle.md)
  The default form style.
- [struct ColumnsFormStyle](columnsformstyle.md)
  A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupedformstyle)*