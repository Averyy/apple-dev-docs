---
url: "https://docs.swift.org/latest/documentation/docc/snippet"
framework: "Swift-Org/docc"
---

# Snippet

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Embeds a code example from the project’s code snippets.

**Availability**:
- Swift-DocC 5.7+

## Declaration

```swift
@Snippet(path: String, slice: String?)
```

#### Overview

Use a `Snippet` directive to embed a code example from the project’s “Snippets” directory on the page. The `path` argument is the relative path from the package’s top-level “Snippets” directory to your snippet file without the `.swift` extension.

```markdown
@Snippet(path: "example-snippet", slice: "setup")
```

If you prefer, you can specify the relative path from the package’s *root* directory (by including a “Snippets/” prefix). You can also include the package name—as defined in `Package.swift`—before the “Snippets/” prefix. Neither of these leading path components are necessary because all your snippet code files are always located in your package’s “Snippets” directory.

> **Earlier Versions**:  Before Swift-DocC 6.2.1, the `@Snippet` path needed to include both the package name component and the “Snippets” component:
>
> ```markdown
> @Snippet(path: "my-package/Snippets/example-snippet")
> ```

You can define named slices of your snippet by annotating the snippet file with `// snippet.<name>` and `// snippet.end` lines. A named slice automatically ends at the start of the next named slice, without an explicit `snippet.end` annotation.

If the referenced snippet includes annotated slices, you can limit the embedded code example to a certain line range by specifying a `slice` name. By default, the embedded code example includes the full snippet. For more information, see [Slice up your snippet to break it up in your content](./adding-code-snippets-to-your-content.md#Slice-up-your-snippet-to-break-it-up-in-your-content).

## Parameters

- `path`: The relative path from your package’s top-level “Snippets” directory to the snippet file that you want to embed in the page, without the `.swift` file extension. **(required)**
- `slice`: The name of a snippet slice to limit the embedded code example to a certain line range. **(optional)**

  By default, the embedded code example includes the full snippet.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/snippet)*