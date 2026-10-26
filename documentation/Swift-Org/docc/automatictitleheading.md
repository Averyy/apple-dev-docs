---
url: "https://docs.swift.org/latest/documentation/docc/automatictitleheading"
framework: "Swift-Org/docc"
---

# AutomaticTitleHeading

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive for specifying Swift-DocC’s automatic behavior when generating a page’s title heading.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@AutomaticTitleHeading(_ enabledness: Enabledness)
```

#### Overview

A title heading is also known as a page eyebrow or kicker.

## Parameters

- `enabledness`: Whether or not DocC generates automatic title headings. **(required)**

  - **`enabled`**: A title heading should be automatically created for the page (the default).
  - **`disabled`**: No automatic title heading should be created for the page.

## See Also

### Adjusting Automatic Behaviors
- [@AutomaticSeeAlso(_ enabledness: Enabledness)](./automaticseealso.md)
  A directive for specifying Swift-DocC’s automatic behavior when generating a page’s See Also section.
- [@AutomaticArticleSubheading(_ enabledness: Enabledness)](./automaticarticlesubheading.md)
  A directive that modifies Swift-DocC’s default behavior for automatic subheading generation on article pages.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/automatictitleheading)*