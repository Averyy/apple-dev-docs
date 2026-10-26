---
url: "https://docs.swift.org/latest/documentation/docc/documentationextension"
framework: "Swift-Org/docc"
---

# DocumentationExtension

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Defines whether the content in a documentation extension file replaces in-source documentation or amends it (the default).

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@DocumentationExtension(mergeBehavior: Behavior)
```

## Mentions

- [Adding Supplemental Content to a Documentation Catalog](./adding-supplemental-content-to-a-documentation-catalog.md)

#### Overview

By default, content from the documentation-extension file is added after the content from the in-source documentation for that symbol.

Swift framework and package APIs are typically documented using comments that reside in-source, alongside the APIs themselves. In some cases, you may wish to supplement or replace in-source documentation with content from dedicated documentation extension files. To learn about this process, see [Adding Supplemental Content to a Documentation Catalog](./adding-supplemental-content-to-a-documentation-catalog.md).

Place the `DocumentationExtension` directive within a `Metadata` directive in a documentation extension file. Set the `mergeBehavior` parameter to `append` or `override` to indicate whether the extension file’s content amends or replaces the in-source documentation.

```markdown
@Metadata {
    @DocumentationExtension(mergeBehavior: override)
}
```

> **Note**:  You can specify a `append` merge behavior but it has the same effect as not defining a `@DocumentationExtension` and results in a warning.

##### Containing Elements

The following items can include a documentation extension element:

- [`Metadata`](./metadata.md)

## Parameters

- `mergeBehavior`: A value of `override` to replace the in-source documentation with the extension file’s content. **(required)**


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/documentationextension)*