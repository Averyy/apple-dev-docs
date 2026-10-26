---
url: "https://docs.swift.org/latest/documentation/docc/titleheading"
framework: "Swift-Org/docc"
---

# TitleHeading

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that specifies a title heading for a given documentation page.

**Availability**:
- Swift-DocC 5.9+

## Declaration

```swift
@TitleHeading(_ heading: String)
```

#### Overview

Place the `TitleHeading` directive within a `Metadata` directive to configure a documentation page to show a custom title heading. Custom title headings, along with custom [page icons](./pageimage.md) and [page colors](./pagecolor.md), allow for the creation of custom kinds of pages beyond just articles.

A title heading is also known as a page eyebrow or kicker.

```markdown
# ``SlothCreator``

@Metadata {
    @TitleHeading("Release Notes")
}
```

A custom title heading appears in place of the page kind at the top of the page.

##### Containing Elements

The following items can include a title heading element:

- [`Metadata`](./metadata.md)
  Use metadata directives to instruct DocC how to build certain documentation files.

## Parameters

- `heading`: The text for the custom title heading.

## See Also

### Customizing the Presentation of a Page
- [@DisplayName(_ name: String, style: Style)](./displayname.md)
  Configures a symbol’s documentation page and any references to that page to show a custom name instead of the symbol name.
- [@PageImage(purpose: Purpose, source: ResourceReference, alt: String)](./pageimage.md)
  Associates an image with a page.
- [@PageKind(_ kind: Kind)](./pagekind.md)
  A directive that allows you to set a page’s kind, which affects its default title heading and page icon.
- [@PageColor(_ color: Color)](./pagecolor.md)
  A directive that specifies an accent color for a given documentation page.
- [@CallToAction(url: URL, file: ResourceReference, purpose: Purpose, label: String)](./calltoaction.md)
  A directive that adds a prominent button or link to a page’s header.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/titleheading)*