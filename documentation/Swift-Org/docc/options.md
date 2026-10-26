---
url: "https://docs.swift.org/latest/documentation/docc/options"
framework: "Swift-Org/docc"
---

# Options

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive to adjust Swift-DocC’s default behaviors when rendering a page.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@Options(scope: Scope = local) {
    ...
}
```

## Parameters

- `scope`: Whether the options in this Options directive should apply locally to the page or globally to the DocC catalog. **(optional)**

  - **`local`**: The directive should only affect the current page.
  - **`global`**: The directive should affect all pages in the current DocC catalog.

## Topics

### Adjusting Automatic Behaviors
- [@AutomaticSeeAlso(_ enabledness: Enabledness)](./automaticseealso.md)
  A directive for specifying Swift-DocC’s automatic behavior when generating a page’s See Also section.
- [@AutomaticTitleHeading(_ enabledness: Enabledness)](./automatictitleheading.md)
  A directive for specifying Swift-DocC’s automatic behavior when generating a page’s title heading.
- [@AutomaticArticleSubheading(_ enabledness: Enabledness)](./automaticarticlesubheading.md)
  A directive that modifies Swift-DocC’s default behavior for automatic subheading generation on article pages.
### Adjusting Visual Style
- [@TopicsVisualStyle(_ style: Style)](./topicsvisualstyle.md)
  A directive for specifying the style that should be used when rendering a page’s Topics section.

## See Also

### Configuring Documentation Behavior
- [@Metadata](./metadata.md)
  Use metadata directives to instruct DocC how to build certain documentation files.
- [@TechnologyRoot](./technologyroot.md)
  Configures an article to become a top-level page.
- [@Redirected(from: URL)](./redirected.md)
  A directive that specifies a previous URL for the page where the directive appears.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/options)*