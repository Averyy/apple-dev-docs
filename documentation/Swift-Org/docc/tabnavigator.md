---
url: "https://docs.swift.org/latest/documentation/docc/tabnavigator"
framework: "Swift-Org/docc"
---

# TabNavigator

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A container directive that arranges content into a tab-based layout.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@TabNavigator {
    @Tab(_ title: String) { ... }
}
```

## Overview

Create a new tab navigator by writing a `@TabNavigator` directive that contains child `@Tab` directives.

```md
@TabNavigator {
   @Tab("Powers") {
      ![A diagram with the five sloth power types.](sloth-powers)
   }

   @Tab("Exercise routines") {
      ![A sloth relaxing and enjoying a good book.](sloth-exercise)
   }

   @Tab("Hats") {
      ![A sloth discovering newfound confidence after donning a fedora.](sloth-hats)
   }
}
```

## Topics

- [@Tab(_ title: String)](./tab.md)
  A container directive that holds general markup content describing an individual tab within a tab-based layout.

## See Also

### Creating Custom Page Layouts
- [@Row(numberOfColumns: Int)](./row.md)
  A container directive that arranges content into a grid-based row and column layout.
- [@Links(visualStyle: VisualStyle)](./links.md)
  A directive for authoring authoring embedded previews of documentation links (similar to how links are currently rendered in Topics sections) anywhere on the page without affecting page curation behavior.
- [@Small](./small.md)
  A directive for specifying small print text like legal, license, or copyright text that should be rendered in a smaller font size.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/tabnavigator)*