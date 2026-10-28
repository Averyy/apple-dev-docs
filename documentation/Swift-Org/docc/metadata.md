---
url: "https://docs.swift.org/latest/documentation/docc/metadata"
framework: "Swift-Org/docc"
---

# Metadata

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Use metadata directives to instruct DocC how to build certain documentation files.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Metadata {
    ...
}
```

## Overview

Use the `Metadata` directive with other directives to configure how certain documentation files build. Place the directive after the documentation page’s title.

Use it with the [`DocumentationExtension`](./documentationextension.md) directive to replace in-source documentation with the documentation extension file’s content.

```markdown
# ``SlothCreator/Sloth``

@Metadata {
    @DocumentationExtension(mergeBehavior: override)
}
```

Use the `Metadata` directive with the [`TechnologyRoot`](./technologyroot.md) directive to customize which article is the top-level page for a documentation catalog (’.docc’ directory) without any framework documentation or other top-level pages.

Use the `Metadata` directive with the [`DisplayName`](./displayname.md) directive to configure a symbol’s documentation page to use a custom display name.

```markdown
# ``SlothCreator``

@Metadata {
    @DisplayName("Sloth Creator")
}
```

Use the `Metadata` directive with the [`TitleHeading`](./titleheading.md) directive to configure the text of a page’s title heading.

```markdown
# ``SlothCreator``

@Metadata {
    @TitleHeading("Release Notes")
}
```

Starting with version 6.0, use the `Metadata` directive with one or more [`Redirected`](./redirected.md) directives to add additional URLs for a page.

```markdown
# ``SlothCreator``

@Metadata {
    @Redirected(from: "old/path/to/page")
    @Redirected(from: "another/old/path/to/page")
}
```

> **Note**: Starting with version 6.0, @Redirected is supported as a child directive of @Metadata. In previous versions, @Redirected must be used as a top level directive.

### Usage in documentation comments

You can specify `@Metadata` configuration in documentation comments to specify [`Available`](./available.md) directives. Other metadata directives are not supported in documentation comments.

> **Note**: Don’t specify an `@Metadata` directive in both the symbol’s documentation comment and its documentation extension file. If you have one in each, DocC will pick the one in the documentation extension and discard the one in the documentation comment.

> **Earlier versions**: Before Swift-DocC 6.1, `@Metadata` was not supported in documentation comments.

## Topics

### Extending or Overriding Source Documentation
- [@DocumentationExtension(mergeBehavior: Behavior)](./documentationextension.md)
  Defines whether the content in a documentation extension file replaces in-source documentation or amends it (the default).
### Creating a Top-Level Technology Page
- [@TechnologyRoot](./technologyroot.md)
  Configures an article to become a top-level page.
### Customizing the Presentation of a Page
- [@DisplayName(_ name: String, style: Style)](./displayname.md)
  Configures a symbol’s documentation page and any references to that page to show a custom name instead of the symbol name.
- [@PageImage(purpose: Purpose, source: ResourceReference, alt: String)](./pageimage.md)
  Associates an image with a page.
- [@PageKind(_ kind: Kind)](./pagekind.md)
  A directive that allows you to set a page’s kind, which affects its default title heading and page icon.
- [@PageColor(_ color: Color)](./pagecolor.md)
  A directive that specifies an accent color for a given documentation page.
- [@CallToAction(url: URL, file: ResourceReference, purpose: Purpose, label: String)](./calltoaction.md)
  A directive that adds a prominent button or link to a page’s header.
- [@TitleHeading(_ heading: String)](./titleheading.md)
  A directive that specifies a title heading for a given documentation page.
### Customizing the Languages of an Article
- [@SupportedLanguage(_ language: SourceLanguage)](./supportedlanguage.md)
  A directive that controls what programming languages an article is available in.
- [@AlternateRepresentation(_ reference: TopicReference)](./alternaterepresentation.md)
  A directive that configures an alternate language representation of a symbol.
### Customizing the Availability Information of a Page
- [@Available(_ platform: Platform, introduced: SemanticVersion, deprecated: SemanticVersion)](./available.md)
  A directive that specifies when a documentation page is available for a given platform.
- [@DeprecationSummary](./deprecationsummary.md)
  A directive that specifies a custom deprecation summary message to an already deprecated symbol.
### Specifying an Additional URL of a Page
- [@Redirected(from: URL)](./redirected.md)
  A directive that specifies a previous URL for the page where the directive appears.

## See Also

### Configuring Documentation Behavior
- [@Options(scope: Scope)](./options.md)
  A directive to adjust Swift-DocC’s default behaviors when rendering a page.
- [@TechnologyRoot](./technologyroot.md)
  Configures an article to become a top-level page.
- [@Redirected(from: URL)](./redirected.md)
  A directive that specifies a previous URL for the page where the directive appears.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/metadata)*