---
url: "https://docs.swift.org/latest/documentation/docc/api-reference-syntax"
framework: "Swift-Org/docc"
---

# API Documentation

**Framework**: Swift-Org/docc  
**Role**: API Collection

Teach your APIs through reference documentation you create from code comments and extension files, or create detailed articles and conceptual guides.

#### Overview

Use documentation markup, a custom variant of Markdown, to add in-source documentation to your APIs. Then, use DocC to build your documentation and share it with developers.

![A screenshot showing the rendered documentation for the SlothCreator framework, including the overview and a partially obscured image.](https://docs.swift.org/latest/images/org.swift.docc/2_docs@2x.png)

## Topics

### Configuring Documentation Behavior
- [@Options(scope: Scope)](./options.md)
  A directive to adjust Swift-DocC’s default behaviors when rendering a page.
- [@Metadata](./metadata.md)
  Use metadata directives to instruct DocC how to build certain documentation files.
- [@TechnologyRoot](./technologyroot.md)
  Configures an article to become a top-level page.
- [@Redirected(from: URL)](./redirected.md)
  A directive that specifies a previous URL for the page where the directive appears.
### Creating Custom Page Layouts
- [@Row(numberOfColumns: Int)](./row.md)
  A container directive that arranges content into a grid-based row and column layout.
- [@TabNavigator](./tabnavigator.md)
  A container directive that arranges content into a tab-based layout.
- [@Links(visualStyle: VisualStyle)](./links.md)
  A directive for authoring authoring embedded previews of documentation links (similar to how links are currently rendered in Topics sections) anywhere on the page without affecting page curation behavior.
- [@Small](./small.md)
  A directive for specifying small print text like legal, license, or copyright text that should be rendered in a smaller font size.

## See Also

### Documentation Types
- [Interactive Tutorials](./tutorial-syntax.md)
  Teach developers your Swift APIs through step-by-step, interactive content.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/api-reference-syntax)*