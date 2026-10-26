---
url: "https://docs.swift.org/latest/documentation/docc/deprecationsummary"
framework: "Swift-Org/docc"
---

# DeprecationSummary

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that specifies a custom deprecation summary message to an already deprecated symbol.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@DeprecationSummary {
    ...
}
```

#### Overview

Many in-source deprecation annotations—such as the `@available` attribute in Swift—allow you to specify a plain text deprecation message. You can use the `@DeprecationSummary` directive to override that deprecation message with one or more paragraphs of formatted documentation markup. For example,

```md
@DeprecationSummary {
    This method is unsafe because it could potentially cause buffer overruns.
    Use ``getBytes(_:length:)`` or ``getBytes(_:range:)`` instead.
}
```

You can use the `@DeprecationSummary` directive top-level in articles, documentation extension files, or documentation comments.

> **Earlier versions**: Before Swift-DocC 6.1, `@DeprecationSummary` was not supported in documentation comments.

> 💡 **Tip**:  If you are writing a custom deprecation summary message for an API or documentation page that isn’t already deprecated, you should also deprecate it—using in-source annotations when possible or [`Available`](./available.md) directives when in-source annotations aren’t available—so that the reader knows the version when you deprecated that API or documentation page.

## See Also

### Customizing the Availability Information of a Page
- [@Available(_ platform: Platform, introduced: SemanticVersion, deprecated: SemanticVersion)](./available.md)
  A directive that specifies when a documentation page is available for a given platform.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/deprecationsummary)*