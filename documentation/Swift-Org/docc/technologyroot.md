---
url: "https://docs.swift.org/latest/documentation/docc/technologyroot"
framework: "Swift-Org/docc"
---

# TechnologyRoot

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Configures an article to become a top-level page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@TechnologyRoot
```

## Overview

If your documentation only consists of articles, without any framework documentation or other top-level pages, DocC will use the only article or the article with the same base name as the documentation catalog (’.docc’ directory) as the top-level page. If the documentation doesn’t contain an article with the same base name as the documentation catalog, DocC will synthesize a minimal top-level page.

To customize which article is the top-level page of your documentation, add a `TechnologyRoot` directive within a `Metadata` directive in that article:

```md
# Page Title

@Metadata {
   @TechnologyRoot
}
```

> **Earlier Versions**:  Before Swift-DocC 6.0, article-only documentation catalogs require one of the articles to be marked as a `TechnologyRoot`.

### Containing Elements

The following items can include a technology root element:

- [`Metadata`](./metadata.md)

## See Also

### Related Documentation
- [Formatting Your Documentation Content](./formatting-your-documentation-content.md)
  Enhance your content’s presentation with special formatting and styling for text and lists.
### Configuring Documentation Behavior
- [@Options(scope: Scope)](./options.md)
  A directive to adjust Swift-DocC’s default behaviors when rendering a page.
- [@Metadata](./metadata.md)
  Use metadata directives to instruct DocC how to build certain documentation files.
- [@Redirected(from: URL)](./redirected.md)
  A directive that specifies a previous URL for the page where the directive appears.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/technologyroot)*