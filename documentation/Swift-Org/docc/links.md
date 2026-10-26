---
url: "https://docs.swift.org/latest/documentation/docc/links"
framework: "Swift-Org/docc"
---

# Links

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive for authoring authoring embedded previews of documentation links (similar to how links are currently rendered in Topics sections) anywhere on the page without affecting page curation behavior.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@Links(visualStyle: VisualStyle) {
    ...
}
```

#### Overview

`@Links` gives authors flexibility in choosing how they want to highlight documentation on the page itself versus in the navigation sidebar. It also allows for mixing and matching different visual styles of topics.

```md
...

### What's New in SlothCreator

@Links(visualStyle: compactGrid) {
   - <doc:get-started-preparing-sloth-food>
   - <doc:feeding-your-sloth-in-winter>
   - <doc:ordering-food-delivery>
}

...
```

## Parameters

- `visualStyle`: The specified style that should be used when rendering the specified links. **(required)**

  - **`list`**: A list of the linked pages, including their full declaration and abstract.
  - **`compactGrid`**: A grid of items based on the card image for the linked pages.

    Includes each page’s title and card image but excludes their abstracts.
  - **`detailedGrid`**: A grid of items based on the card image for the linked pages.

    Unlike `compactGrid`, this style includes the abstract for each page.

## See Also

### Creating Custom Page Layouts
- [@Row(numberOfColumns: Int)](./row.md)
  A container directive that arranges content into a grid-based row and column layout.
- [@TabNavigator](./tabnavigator.md)
  A container directive that arranges content into a tab-based layout.
- [@Small](./small.md)
  A directive for specifying small print text like legal, license, or copyright text that should be rendered in a smaller font size.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/links)*