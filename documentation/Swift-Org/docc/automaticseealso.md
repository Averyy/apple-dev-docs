---
url: "https://docs.swift.org/latest/documentation/docc/automaticseealso"
framework: "Swift-Org/docc"
---

# AutomaticSeeAlso

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive for specifying Swift-DocC’s automatic behavior when generating a page’s See Also section.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@AutomaticSeeAlso(_ enabledness: Enabledness)
```

## Parameters

- `enabledness`: Whether or not DocC generates automatic See Also sections. **(required)**

  - **`enabled`**: A See Also section should be automatically created (the default).
  - **`disabled`**: No automatic See Also section should be created.

## See Also

### Adjusting Automatic Behaviors
- [@AutomaticTitleHeading(_ enabledness: Enabledness)](./automatictitleheading.md)
  A directive for specifying Swift-DocC’s automatic behavior when generating a page’s title heading.
- [@AutomaticArticleSubheading(_ enabledness: Enabledness)](./automaticarticlesubheading.md)
  A directive that modifies Swift-DocC’s default behavior for automatic subheading generation on article pages.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/automaticseealso)*