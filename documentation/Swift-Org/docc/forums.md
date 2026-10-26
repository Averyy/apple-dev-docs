---
url: "https://docs.swift.org/latest/documentation/docc/forums"
framework: "Swift-Org/docc"
---

# Forums

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a set of forum links in the resources section of a tutorial’s table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Forums(...) {
    ...
}
```

#### Overview

Use the `Forums` directive to add links to related forums in the Resources section at the bottom of your tutorial’s table of contents page.

DocC renders the URL you specify in the `destination` parameter as a “View forums” link at the bottom of the forums section. Within the directive, add descriptive text and, optionally, use standard Markdown syntax to provide links to one or more more specific forums.

A single “View forums” link:

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @Forums(destination: "https://www.example.com/sloth-forums/") {
            Get support for your sloths and connect with others.
        }
    }
}
```

A “View forums” link with additional specific forum links:

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @Forums(destination: "https://www.example.com/sloth-forums/") {
            Get support for your sloths and connect with others.

            - [SlothCreator Help: Get Assistance with Sloth Development.](https://www.example.com/sloth-forums/help/)
            - [Sloth Talk: Meet Others Who Like Sloths Too](https://www.example.com/sloth-forums/speedy/)
        }
    }
}
```

You can include forum links alongside other types of resources, like [`Documentation`](./documentation.md),  [`Downloads`](./downloads.md), [`SampleCode`](./samplecode.md), and [`Videos`](./videos.md).

##### Containing Elements

The following items can contain forum resources:

- [`Resources`](./resources.md)

## Parameters

- `destination`: A URL to a page of related forums. **(required)**

## See Also

### Displaying Resources
- [@Documentation(...)](./documentation.md)
  Displays a set of documentation links in the resources section of a tutorial’s table of contents page.
- [@Downloads(...)](./downloads.md)
  Displays a set of related download links in the resources section of a tutorial’s table of contents page.
- [@SampleCode(...)](./samplecode.md)
  Displays a set of sample code links in the resources section of a tutorial’s table of contents page.
- [@Videos(...)](./videos.md)
  Displays a set of video links in the resources section of a tutorial’s table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/forums)*