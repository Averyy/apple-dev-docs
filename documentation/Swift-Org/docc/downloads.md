---
url: "https://docs.swift.org/latest/documentation/docc/downloads"
framework: "Swift-Org/docc"
---

# Downloads

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a set of related download links in the resources section of a tutorial’s table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Downloads(...) {
    ...
}
```

#### Overview

Use the `Downloads` directive to add links to related downloads in the resources section at the bottom of your tutorial’s table of contents page.

DocC renders the URL you specify in the `destination` parameter as a “View downloads” link at the bottom of the downloads section. Within the directive, add descriptive text and, optionally, use standard Markdown syntax to provide links to one or more more specific downloads or download pages.

A single “View downloads” link:

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @Downloads(destination: "https://www.example.com/sloth-downloads/") {
            Download resources that make sloth development even more fun.
        }

    }

}
```

A “View downloads” link with additional specific download links:

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @Downloads(destination: "https://www.example.com/sloth-downloads/") {
            Download resources that make sloth development even more fun.

            - [Sloth Wallpaper](https://www.example.com/sloth-downloads/wallpaper/)
            - [Sloth Coloring Pages](https://www.example.com/sloth-downloads/coloring/)
            - [Sloth Apps](https://www.example.com/sloth-downloads/apps/)
        }

    }

}
```

You can include downloads alongside other types of resources, like [`Documentation`](./documentation.md),  [`Forums`](./forums.md), [`SampleCode`](./samplecode.md), and [`Videos`](./videos.md).

##### Containing Elements

The following items can contain download resources:

- [`Resources`](./resources.md)

## Parameters

- `destination`: A URL to a page of related downloads. **(required)**

## See Also

### Displaying Resources
- [@Documentation(...)](./documentation.md)
  Displays a set of documentation links in the resources section of a tutorial’s table of contents page.
- [@Forums(...)](./forums.md)
  Displays a set of forum links in the resources section of a tutorial’s table of contents page.
- [@SampleCode(...)](./samplecode.md)
  Displays a set of sample code links in the resources section of a tutorial’s table of contents page.
- [@Videos(...)](./videos.md)
  Displays a set of video links in the resources section of a tutorial’s table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/downloads)*