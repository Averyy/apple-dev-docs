# AutomaticFormStyle

**Framework**: SwiftUI  
**Kind**: struct

The default form style.

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
struct AutomaticFormStyle
```

#### Overview

Use the [`automatic`](formstyle/automatic.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.automatic)
```

## Topics

### Creating the form style
- [init()](automaticformstyle/init.md)
  Creates a default form style.

## Relationships

### Conforms To
- [FormStyle](formstyle.md)

## See Also

- [struct ColumnsFormStyle](columnsformstyle.md)
  A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [struct GroupedFormStyle](groupedformstyle.md)
  A form style with grouped rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/automaticformstyle)*