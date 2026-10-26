---
url: "https://docs.swift.org/latest/documentation/docc/pagecolor"
framework: "Swift-Org/docc"
---

# PageColor

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that specifies an accent color for a given documentation page.

**Availability**:
- Swift-DocC 5.9+

## Declaration

```swift
@PageColor(_ color: Color)
```

## Mentions

- [Customizing the Appearance of Your Documentation Pages](./customizing-the-appearance-of-your-documentation-pages.md)

#### Overview

Use the `PageColor` directive to provide a hint to the renderer as to how the page should be accented with color. The renderer may use this color, depending on the context, as a foundation for other colors used on the page. For example, Swift-DocC-Render uses this color as the primary background color of a page’s introduction section and adjusts other elements in the introduction section to account for the new background.

This directive is only valid within a [`Metadata`](./metadata.md) directive:

```markdown
@Metadata {
    @PageColor(orange)
}
```

## Parameters

- `color`: A context-dependent, standard color. **(required)**

  - **`blue`**: A context-dependent blue color.
  - **`gray`**: A context-dependent gray color.
  - **`green`**: A context-dependent green color.
  - **`orange`**: A context-dependent orange color.
  - **`purple`**: A context-dependent purple color.
  - **`red`**: A context-dependent red color.
  - **`yellow`**: A context-dependent yellow color.

## See Also

### Customizing the Presentation of a Page
- [@DisplayName(_ name: String, style: Style)](./displayname.md)
  Configures a symbol’s documentation page and any references to that page to show a custom name instead of the symbol name.
- [@PageImage(purpose: Purpose, source: ResourceReference, alt: String)](./pageimage.md)
  Associates an image with a page.
- [@PageKind(_ kind: Kind)](./pagekind.md)
  A directive that allows you to set a page’s kind, which affects its default title heading and page icon.
- [@CallToAction(url: URL, file: ResourceReference, purpose: Purpose, label: String)](./calltoaction.md)
  A directive that adds a prominent button or link to a page’s header.
- [@TitleHeading(_ heading: String)](./titleheading.md)
  A directive that specifies a title heading for a given documentation page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/pagecolor)*