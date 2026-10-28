---
url: "https://docs.swift.org/latest/documentation/docc/displayname"
framework: "Swift-Org/docc"
---

# DisplayName

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Configures a symbol’s documentation page and any references to that page to show a custom name instead of the symbol name.

**Availability**:
- Swift-DocC 5.7+

## Declaration

```swift
@DisplayName(_ name: String, style: Style = conceptual)
```

## Overview

Place the `DisplayName` directive within a `Metadata` directive to configure a symbol’s documentation page and any references to that page to show a custom name.

```markdown
# ``SlothCreator``

@Metadata {
    @DisplayName("Sloth Creator")
}
```

A custom display name appears in place of the symbol’s name in the following locations:

- The main header on the symbol page
- The navigator hierarchy
- Breadcrumbs for the symbol page and its child symbol pages
- Link text anywhere that includes a link to the symbol page

> **Note**: Customizing the name of a symbol page doesn’t alter the page’s URL.

By default, a custom display name renders without a monospaced text style. To retain the monospaced text style that’s typically used when referencing APIs, specify a value of `symbol` for the optional `style` parameter:

```markdown
# ``SlothCreator``

@Metadata {
    @DisplayName("Sloth Creator", style: symbol)
}
```

> **Note**: Adding a `DisplayName` directive to a non-symbol page results in a warning.

### Containing Elements

The following items can include a display name element:

- [`Metadata`](./metadata.md)

## Parameters

- `name`: The custom display name.
- `style`: The text style used to format the symbol’s display name. A value of `conceptual` (the default) denotes a plain text style that’s not monospaced. A value of `symbol` denotes a monospaced text style. **(optional)**

## See Also

### Customizing the Presentation of a Page
- [@PageImage(purpose: Purpose, source: ResourceReference, alt: String)](./pageimage.md)
  Associates an image with a page.
- [@PageKind(_ kind: Kind)](./pagekind.md)
  A directive that allows you to set a page’s kind, which affects its default title heading and page icon.
- [@PageColor(_ color: Color)](./pagecolor.md)
  A directive that specifies an accent color for a given documentation page.
- [@CallToAction(url: URL, file: ResourceReference, purpose: Purpose, label: String)](./calltoaction.md)
  A directive that adds a prominent button or link to a page’s header.
- [@TitleHeading(_ heading: String)](./titleheading.md)
  A directive that specifies a title heading for a given documentation page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/displayname)*