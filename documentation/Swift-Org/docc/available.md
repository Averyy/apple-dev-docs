---
url: "https://docs.swift.org/latest/documentation/docc/available"
framework: "Swift-Org/docc"
---

# Available

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that specifies when a documentation page is available for a given platform.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@Available(_ platform: Platform, introduced: SemanticVersion, deprecated: SemanticVersion?)
```

## Overview

Whenever possible, prefer to specify availability information using in-source annotations such as the `@available` attribute in Swift or the `API_AVAILABLE` macro in Objective-C. Using in-source annotations ensures that your documentation matches the availability of your API. If you duplicate availability information in the documentation markup, the information from the `@Available` directive overrides the information for the in-source annotations from that platform and risks being inaccurate.

If your source language doesn’t have a mechanism for specifying API availability or if you’re writing articles about a newly introduced or deprecated API, you can use the `@Available` directive to specify when you introduced, and optionally deprecated, an API or documentation page for a given platform.

Each `@Available` directive specifies the availability information for a single platform. The directive matches the `iOS`, `macOS`, `watchOS`, and `tvOS` platform names case-insensitively. Any other platform names are displayed verbatim. If a platform name contains whitespace, commas, or other special characters you need to surround it with quotation marks (`"`).

```markdown
@Metadata {
    @Available(iOS, introduced: "15.0")
    @Available(macOS, introduced: "12.0", deprecated: "14.0")
    @Available("My Package", introduced: "1.2.3")
}
```

Both the “introduced” and “deprecated” parameters take string representations of semantic version numbers (major`.`minor`.`patch). If you omit the “patch” or “minor” components, they are assumed to be `0`. This means that `"1.0.0"`, `"1.0"`, and `"1"` all specify the same semantic version.

> **Earlier Versions**:  Before Swift-DocC 6.0, the `@Available` directive didn’t support the “deprecated” parameter.

> 💡 **Tip**:  In addition to specifying the version when you deprecated an API or documentation page, you can use the [`DeprecationSummary`](./deprecationsummary.md) directive to provide the reader with additional information about the deprecation or refer them to a replacement API.

## Parameters

- `platform`: The platform name that this version information applies to. **(required)**
- `introduced`: The semantic version (major`.`minor`.`patch) when you introduced this API or documentation page. **(required)**
- `deprecated`: The semantic version (major`.`minor`.`patch) when you deprecated this API or documentation page. **(optional)**

## See Also

### Customizing the Availability Information of a Page
- [@DeprecationSummary](./deprecationsummary.md)
  A directive that specifies a custom deprecation summary message to an already deprecated symbol.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/available)*