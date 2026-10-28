---
url: "https://docs.swift.org/latest/documentation/docc/redirected"
framework: "Swift-Org/docc"
---

# Redirected

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive that specifies a previous URL for the page where the directive appears.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Redirected(from: URL)
```

## Overview

If the page has moved more than once you can add multiple  `Redirected` directives, each specifying one previous URL. For example:

```md
@Redirected(from: "old/path/to/this/page")
@Redirected(from: "another/old/path/to/this/page")
```

> **Note**: Starting with version 6.0, the `Redirected` directive is supported both top-level and as a member of a [`Metadata`](./metadata.md) directive. In earlier versions, the `Redirected` directive is only supported as a top-level directive.

### Setting up Redirects

If you host your documentation on a web server, you can set a HTTP “301 Moved Permanently” redirect for each `Redirected` value to avoid breaking existing links to your content.

To find each page’s Redirected values, pass the `--emit-digest` flag to DocC. This flag configures DocC to write additional metadata files to the output directory. One of these files, `linkable-entities.json`, contains summarized information about all pages and on-page landmarks that you can link to from outside the DocC documentation. Each of these “entities” has a `"path"`—which represents the current relative path of that page—and an optional list of `"redirects"`—which represent all the `Redirected` values for page as they were authored in the markup. You can write either relative redirect values or absolute redirect values in the markup depending on what information you need when setting up HTTP “301 Moved Permanently” redirects on your web server.

## Parameters

- `from`: The URL that redirects to the page associated with the directive. **(required)**

## See Also

### Configuring Documentation Behavior
- [@Options(scope: Scope)](./options.md)
  A directive to adjust Swift-DocC’s default behaviors when rendering a page.
- [@Metadata](./metadata.md)
  Use metadata directives to instruct DocC how to build certain documentation files.
- [@TechnologyRoot](./technologyroot.md)
  Configures an article to become a top-level page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/redirected)*