---
url: "https://docs.swift.org/latest/documentation/docc/resources"
framework: "Swift-Org/docc"
---

# Resources

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a set of links to related resources, like downloads, sample code, and videos.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Resources {
    ...
}
```

## Overview

Use the `Resources` directive to include a Resources section at the bottom of a tutorial’s table of contents page. This optional section can offer links to helpful material for continued learning. Provide some text for the top of the section, then add directives, for example [`Documentation`](./documentation.md), [`Downloads`](./downloads.md), [`Forums`](./forums.md), [`SampleCode`](./samplecode.md), and [`Videos`](./videos.md)) for the resource types you want to share.

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

        @Downloads(destination: "https://www.example.com/images/sloth-wallpaper/") {
            Download the cutest sloth wallpaper for your iPhone, iPad, or Mac.
        }
    }
}
```

### Contained Elements

A Resources section can contain the following items:

- **[`Documentation`](./documentation.md)**: Displays one or more links to related documentation. **(optional)**
- **[`Downloads`](./downloads.md)**: Displays one or more links to related downloads. **(optional)**
- **[`Forums`](./forums.md)**: Displays one or more links to related forums. **(optional)**
- **[`SampleCode`](./samplecode.md)**: Displays one or more links to related sample code. **(optional)**
- **[`Videos`](./videos.md)**: Displays one or more links to related videos. **(optional)**

### Containing Elements

The following pages can include a Resources section:

- [`Tutorials`](./tutorials.md)

## Topics

### Displaying Resources
- [@Documentation(...)](./documentation.md)
  Displays a set of documentation links in the resources section of a tutorial’s table of contents page.
- [@Downloads(...)](./downloads.md)
  Displays a set of related download links in the resources section of a tutorial’s table of contents page.
- [@Forums(...)](./forums.md)
  Displays a set of forum links in the resources section of a tutorial’s table of contents page.
- [@SampleCode(...)](./samplecode.md)
  Displays a set of sample code links in the resources section of a tutorial’s table of contents page.
- [@Videos(...)](./videos.md)
  Displays a set of video links in the resources section of a tutorial’s table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/resources)*