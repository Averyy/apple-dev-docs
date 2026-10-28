---
url: "https://docs.swift.org/latest/documentation/docc/row"
framework: "Swift-Org/docc"
---

# Row

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A container directive that arranges content into a grid-based row and column layout.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@Row(numberOfColumns: Int?) {
    @Column(size: Int = 1) { ... }
}
```

## Overview

Create a new row by creating an `@Row` that contains child `@Column` directives.

```md
@Row {
   @Column {
      @Image(source: "icon-power-icon", alt: "A blue square containing a snowflake.") {
         Ice power
      }
   }

   @Column {
      @Image(source: "fire-power-icon", alt: "A red square containing a flame.") {
         Fire power
      }
   }

   @Column {
      @Image(source: "wind-power-icon", alt: "A teal square containing a breath of air.") {
         Wind power
      }
   }

   @Column {
      @Image(source: "lightning-power-icon", alt: "A yellow square containing a lightning bolt.") {
         Lightning power
      }
   }
}
```

## Parameters

- `numberOfColumns`: The number of columns available in this row. **(optional)**

## Topics

- [@Column(size: Int)](./column.md)
  A container directive that holds general markup content describing a column with a row in a grid-based layout.

## See Also

### Creating Custom Page Layouts
- [@TabNavigator](./tabnavigator.md)
  A container directive that arranges content into a tab-based layout.
- [@Links(visualStyle: VisualStyle)](./links.md)
  A directive for authoring authoring embedded previews of documentation links (similar to how links are currently rendered in Topics sections) anywhere on the page without affecting page curation behavior.
- [@Small](./small.md)
  A directive for specifying small print text like legal, license, or copyright text that should be rendered in a smaller font size.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/row)*