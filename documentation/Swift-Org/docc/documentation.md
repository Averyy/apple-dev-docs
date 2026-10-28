---
url: "https://docs.swift.org/latest/documentation/docc/documentation"
framework: "Swift-Org/docc"
---

# Documentation

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a set of documentation links in the resources section of a tutorial’s table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Documentation(...) {
    ...
}
```

## Overview

Use the `Documentation` directive to add links to related documentation in the Resources section at the bottom of your tutorial’s table of contents page.

DocC renders the URL you specify in the `destination` parameter as a “View more” link at the bottom of the documentation section. Within the directive, add descriptive text and use standard Markdown syntax to provide links to one or more specific documentation pages. At least one specific documentation link within the directive is required.

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @Documentation(destination: "https://www.example.com/sloth-docs/") {
            Browse and search sloth-related documentation.

            - [SlothCreator API](https://www.example.com/sloth-docs/slothcreator/)
            - [Sloth Technical Specification](https://www.example.com/sloth-docs/sloth-spec/)
        }

    }

}
```

You can include documentation alongside other types of resources, like [`Downloads`](./downloads.md),  [`Forums`](./forums.md), [`SampleCode`](./samplecode.md), and [`Videos`](./videos.md).

### Containing Elements

The following items can contain documentation resources:

- [`Resources`](./resources.md)

## Parameters

- `destination`: A URL to a page of related documentation. **(required)**

## See Also

### Displaying Resources
- [@Downloads(...)](./downloads.md)
  Displays a set of related download links in the resources section of a tutorial’s table of contents page.
- [@Forums(...)](./forums.md)
  Displays a set of forum links in the resources section of a tutorial’s table of contents page.
- [@SampleCode(...)](./samplecode.md)
  Displays a set of sample code links in the resources section of a tutorial’s table of contents page.
- [@Videos(...)](./videos.md)
  Displays a set of video links in the resources section of a tutorial’s table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/documentation)*