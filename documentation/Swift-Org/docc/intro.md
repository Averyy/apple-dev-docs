---
url: "https://docs.swift.org/latest/documentation/docc/intro"
framework: "Swift-Org/docc"
---

# Intro

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays an introduction section at the top of a table of contents or tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Intro(title: String) {
    ...
}
```

## Mentions

- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)

#### Overview

You can display an introduction at the top of every table of contents by using the [`Tutorials`](./tutorials.md) directive and at the top of every tutorial page by using the [`Tutorial`](./tutorial.md) directive. It’s the first thing a reader sees on these pages, so it needs to draw them into the content that follows.

Example of an introduction section on a table of contents page:

![A screenshot showing the introduction section on a table of contents page.](https://docs.swift.org/latest/images/org.swift.docc/tutorial-intro-toc@2x.png)

Example of an introduction section on a tutorial page:

![A screenshot showing the introduction section on a tutorial page.](https://docs.swift.org/latest/images/org.swift.docc/tutorial-intro-tutorialpage@2x.png)

Use the `Intro` directive to insert an introduction section. In the `title` parameter, specify a title to show at the top of the introduction. Next, provide some engaging text. Finally, add an `Image` to serve as the section’s background, or a `Video` directive to display a link to an introduction video. See [`Image`](./image.md) and [`Video`](./video.md) for supported media file formats and naming conventions.

```markdown
@Tutorials(name: "SlothCreator") {
    @Intro(title: "Meet SlothCreator") {
        Create, catalog, and care for sloths using SlothCreator.
        Get started with SlothCreator by building the demo app _Slothy_.
        
        @Image(source: slothcreator-intro.png, alt: "An illustration of 3 iPhones in portrait mode, displaying the UI of finding, creating, and taking care of a sloth in Slothy — the sample app that you build in this collection of tutorials.")
    }
    
    ...
    
}
```

DocC automatically adds additional elements to introduction sections during rendering. For example, on a table of contents page, the introduction calculates and displays the total estimated time to complete all pages of the tutorial. It derives this value by combining the time estimates you provide on individual tutorial pages. The table of contents introduction also includes a Get Started button that takes readers to the first tutorial page.

##### Contained Elements

An introduction can contain the following items:

- **[`Image`](./image.md)**: An image to serve as a background. **(optional)**
- **[`Video`](./video.md)**: A link to view an introduction video. **(optional)**

##### Containing Elements

The following pages must include an introduction section:

- [`Tutorial`](./tutorial.md)
- [`Tutorials`](./tutorials.md)

## Parameters

- `title`: A title to show at the top of the introduction. **(required)**

## Topics

### Displaying Media
- [@Image(source: ResourceReference, alt: String)](./image.md)
  Displays an image in a tutorial.
- [@Video(source: ResourceReference, alt: String, poster: ResourceReference)](./video.md)
  Displays a video in a tutorial.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/intro)*