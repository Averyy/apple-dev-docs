---
url: "https://docs.swift.org/latest/documentation/docc/videos"
framework: "Swift-Org/docc"
---

# Videos

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a set of video links in the resources section of a tutorial’s table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Videos(...) {
    ...
}
```

#### Overview

Use the `Videos` directive to add links to related videos in the Resources section at the bottom of your tutorial’s table of contents page.

DocC renders the URL you specify in the `destination` parameter as a “Watch videos” link at the bottom of the sample code section. Within the directive, add descriptive text and, optionally, use standard Markdown syntax to provide links to one or more more specific videos.

A single “Watch videos” link:

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @Videos(destination: "https://www.example.com/sloth-videos/") {
            Watch cute videos of sloths climbing, eating, and sleeping.
        }
    }
}
```

A “Watch videos” link with additional specific video links:

```markdown
@Tutorials(name: "SlothCreator") {
        
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @Videos(destination: "https://www.example.com/sloth-videos/") {
            Watch cute videos of sloths climbing, eating, and sleeping.

            - [Treetop Breakfast](https://www.example.com/sloth-videos/breakfast/)
            - [Slow Ascent](https://www.example.com/sloth-videos/climb/)
            - [Rest Time](https://www.example.com/sloth-videos/snoozing/)
        }
    }
}
```

You can include video links alongside other types of resources, like [`Documentation`](./documentation.md),  [`Downloads`](./downloads.md), [`Forums`](./forums.md), and [`SampleCode`](./samplecode.md).

##### Containing Elements

The following items can contain video resources:

- [`Resources`](./resources.md)

## Parameters

- `destination`: A URL to a page of related videos. **(required)**

## See Also

### Displaying Resources
- [@Documentation(...)](./documentation.md)
  Displays a set of documentation links in the resources section of a tutorial’s table of contents page.
- [@Downloads(...)](./downloads.md)
  Displays a set of related download links in the resources section of a tutorial’s table of contents page.
- [@Forums(...)](./forums.md)
  Displays a set of forum links in the resources section of a tutorial’s table of contents page.
- [@SampleCode(...)](./samplecode.md)
  Displays a set of sample code links in the resources section of a tutorial’s table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/videos)*