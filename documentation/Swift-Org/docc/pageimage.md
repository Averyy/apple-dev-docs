---
url: "https://docs.swift.org/latest/documentation/docc/pageimage"
framework: "Swift-Org/docc"
---

# PageImage

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Associates an image with a page.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@PageImage(purpose: Purpose, source: ResourceReference, alt: String?)
```

## Mentions

- [Customizing the Appearance of Your Documentation Pages](./customizing-the-appearance-of-your-documentation-pages.md)

#### Overview

You can use this directive to set the image used when rendering a user-interface element representing the page.

Use the “icon” purpose to customize the icon that DocC uses to represent this page in the navigation sidebar. For article pages, DocC also uses this icon to represent the article in topics sections and in [`Links`](./links.md) directives that use the `list` visual style.

> 💡 **Tip**: Page images with the “icon” purpose work best when they’re square and when they have good visual clarity at small sizes (less than 20×20 points).

Use the “card” purpose to customize the image that DocC uses to represent this page inside [`Links`](./links.md) directives that use the either the `detailedGrid` or the `compactGrid` visual style. For article pages, DocC also incorporates a partially faded out version of the card image in the background of the page itself.

> 💡 **Tip**: Page images with the “card” purpose work best when they have a 16:9 aspect ratio. Currently, the largest size that DocC displays a card image is 640×360 points.

If you specify an “icon” page image without specifying a “card” page image, DocC will use the icon as a fallback in places where the card image is preferred. To avoid upscaled pixelated icons in these places, either configure a “card” page image as well or use a scalable vector image asset for the “icon” page image.

## Parameters

- `purpose`: The image’s purpose. **(required)**

  - **`icon`**: The image will be used when representing the page as an icon, such as in the navigation sidebar.
  - **`card`**: The image will be used when representing the page as a card, such as in grid styled Topics sections.
- `source`: The base file name of an image in your documentation catalog. **(required)**
- `alt`: Alternative text that describes the image to screen readers. **(optional)**

## See Also

### Customizing the Presentation of a Page
- [@DisplayName(_ name: String, style: Style)](./displayname.md)
  Configures a symbol’s documentation page and any references to that page to show a custom name instead of the symbol name.
- [@PageKind(_ kind: Kind)](./pagekind.md)
  A directive that allows you to set a page’s kind, which affects its default title heading and page icon.
- [@PageColor(_ color: Color)](./pagecolor.md)
  A directive that specifies an accent color for a given documentation page.
- [@CallToAction(url: URL, file: ResourceReference, purpose: Purpose, label: String)](./calltoaction.md)
  A directive that adds a prominent button or link to a page’s header.
- [@TitleHeading(_ heading: String)](./titleheading.md)
  A directive that specifies a title heading for a given documentation page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/pageimage)*