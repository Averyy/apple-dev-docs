---
url: "https://docs.swift.org/latest/documentation/docc/automaticarticlesubheading"
framework: "Swift-Org/docc"
---

# AutomaticArticleSubheading

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that modifies Swift-DocC’s default behavior for automatic subheading generation on article pages.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@AutomaticArticleSubheading(_ enabledness: Enabledness)
```

#### Overview

By default, articles receive a second-level “Overview” heading unless the author explicitly writes some other H2 heading below the abstract. This allows for opting out of that behavior.

## Parameters

- `enabledness`: Whether or not DocC generates automatic second-level “Overview” subheadings. **(required)**

  - **`enabled`**: An overview subheading should be automatically created for the article (the default).
  - **`disabled`**: No automatic overview subheading should be created for the article.

## See Also

### Adjusting Automatic Behaviors
- [@AutomaticSeeAlso(_ enabledness: Enabledness)](./automaticseealso.md)
  A directive for specifying Swift-DocC’s automatic behavior when generating a page’s See Also section.
- [@AutomaticTitleHeading(_ enabledness: Enabledness)](./automatictitleheading.md)
  A directive for specifying Swift-DocC’s automatic behavior when generating a page’s title heading.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/automaticarticlesubheading)*