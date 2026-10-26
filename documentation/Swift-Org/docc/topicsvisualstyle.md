---
url: "https://docs.swift.org/latest/documentation/docc/topicsvisualstyle"
framework: "Swift-Org/docc"
---

# TopicsVisualStyle

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive for specifying the style that should be used when rendering a page’s Topics section.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@TopicsVisualStyle(_ style: Style)
```

## Parameters

- `style`: The specified style that should be used when rendering a page’s Topics section. **(required)**

  - **`list`**: A list of the page’s topics, including their full declaration and abstract.
  - **`compactGrid`**: A grid of items based on the card image for each page.

    Includes each page’s title and card image but excludes their abstracts.
  - **`detailedGrid`**: A grid of items based on the card image for each page.

    Unlike `compactGrid`, this style includes the abstract for each page.
  - **`hidden`**: Do not show child pages anywhere on the page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/topicsvisualstyle)*