---
url: "https://docs.swift.org/latest/documentation/docc/samplecode"
framework: "Swift-Org/docc"
---

# SampleCode

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a set of sample code links in the resources section of a tutorial’s table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@SampleCode(...) {
    ...
}
```

#### Overview

Use the `SampleCode` directive to add links to related sample code in the Resources section at the bottom of your tutorial’s table of contents page.

DocC renders the URL you specify in the `destination` parameter as a “View more” link at the bottom of the sample code section. Within the directive, add descriptive text and use standard Markdown syntax to provide links to one or more more specific sample code pages. At least one specific sample code link within the directive is required.

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Resources {
        Explore more resources for learning about sloths.

        @SampleCode(destination: "https://www.example.com/sloth-code/") {
            Download and explore sample code projects to get to know SlothCreator.

            - [SlothyRoad: Building a Fun, Yet Slow Game](https://www.example.com/sloth-code/slothyroad/)
            - [SpeedySloth: Designing a Faster, More Powerful Sloth](https://www.example.com/sloth-code/speedy/)
            - [SmoothSloth: Adding a Smooth and Glossy Coat to Your Sloth](https://www.example.com/sloth-code/smooth/)
        }
    }
}
```

You can include sample code links alongside other types of resources, like [`Documentation`](./documentation.md),  [`Downloads`](./downloads.md), [`Forums`](./forums.md), and [`Videos`](./videos.md).

##### Containing Elements

The following items can contain sample code resources:

- [`Resources`](./resources.md)

## Parameters

- `destination`: A URL to a page of related sample code. **(required)**

## See Also

### Displaying Resources
- [@Documentation(...)](./documentation.md)
  Displays a set of documentation links in the resources section of a tutorial’s table of contents page.
- [@Downloads(...)](./downloads.md)
  Displays a set of related download links in the resources section of a tutorial’s table of contents page.
- [@Forums(...)](./forums.md)
  Displays a set of forum links in the resources section of a tutorial’s table of contents page.
- [@Videos(...)](./videos.md)
  Displays a set of video links in the resources section of a tutorial’s table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/samplecode)*