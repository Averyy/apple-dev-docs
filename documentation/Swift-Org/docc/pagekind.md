---
url: "https://docs.swift.org/latest/documentation/docc/pagekind"
framework: "Swift-Org/docc"
---

# PageKind

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that allows you to set a page’s kind, which affects its default title heading and page icon.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@PageKind(_ kind: Kind)
```

## Overview

The `@PageKind` directive tells Swift-DocC to treat a documentation page as a particular “kind”. This is used to determine the page’s default navigator icon, as well as the default title heading on the page itself.

The available page kinds are `article` and `sampleCode`.

This directive is only valid within a `@Metadata` directive:

```markdown
@Metadata {
    @PageKind(sampleCode)
}
```

## Parameters

- `kind`: The page kind to apply to the page. **(required)**

  - **`article`**: An article of free-form text; the default for standalone markdown files.
  - **`sampleCode`**: A page describing a “sample code” project.

## See Also

### Customizing the Presentation of a Page
- [@DisplayName(_ name: String, style: Style)](./displayname.md)
  Configures a symbol’s documentation page and any references to that page to show a custom name instead of the symbol name.
- [@PageImage(purpose: Purpose, source: ResourceReference, alt: String)](./pageimage.md)
  Associates an image with a page.
- [@PageColor(_ color: Color)](./pagecolor.md)
  A directive that specifies an accent color for a given documentation page.
- [@CallToAction(url: URL, file: ResourceReference, purpose: Purpose, label: String)](./calltoaction.md)
  A directive that adds a prominent button or link to a page’s header.
- [@TitleHeading(_ heading: String)](./titleheading.md)
  A directive that specifies a title heading for a given documentation page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/pagekind)*