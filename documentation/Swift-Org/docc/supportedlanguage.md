---
url: "https://docs.swift.org/latest/documentation/docc/supportedlanguage"
framework: "Swift-Org/docc"
---

# SupportedLanguage

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that controls what programming languages an article is available in.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@SupportedLanguage(_ language: SourceLanguage)
```

## Overview

By default, an article is available in the languages the module that’s being documented is available in. Use this directive to override this behavior in a [`Metadata`](./metadata.md) directive:

```markdown
@Metadata {
    @SupportedLanguage(swift)
    @SupportedLanguage(objc)
}
```

This directive supports any language identifier, but only the following are currently supported by Swift-DocC Render:

| Identifier | Language |
| --- | --- |
| `swift` | Swift |
| `objc`, `objective-c` | Objective-C |

## Parameters

- `language`: A source language that this symbol is available in. **(required)**

  For supported values, see [`SupportedLanguage`](./supportedlanguage.md).

## See Also

### Customizing the Languages of an Article
- [@AlternateRepresentation(_ reference: TopicReference)](./alternaterepresentation.md)
  A directive that configures an alternate language representation of a symbol.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/supportedlanguage)*