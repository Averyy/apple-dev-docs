---
url: "https://docs.swift.org/latest/documentation/docc/article"
framework: "Swift-Org/docc"
---

# Article

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a tutorial article page that teaches a conceptual topic about your Swift framework or package.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Article(...) {
    ...
}
```

#### Overview

The `Article` directive defines the structure of an individual tutorial article page that teaches a conceptual topic about your Swift framework or package.

A tutorial article supports many of the same directives as a [`Tutorial`](./tutorial.md) directive but doesn’t teach its content through interactive exercise.

##### Contained Elements

A tutorial page can contain the following items:

- **[`Intro`](./intro.md)**: Engaging introductory text and an image or video to display at the top of the page. **(optional)**
- **[`ContentAndMedia`](./contentandmedia.md)**: A grouping that contains text and an image or video. At least one `ContentAndMedia` directive is required and must be the first element within a section. **(optional)**
- **[`Stack`](./stack.md)**: A set of horizontally arranged groupings of text and media. **(optional)**
- **[`Assessments`](./assessments.md)**: Assessments that test the reader’s knowledge about the content described in the article. **(optional)**
- **[`Image`](./image.md)**: An image that appears on the page. **(optional)**

## Parameters

- `time`: An integer value that represents the estimated time it takes to complete the tutorial, in minutes. **(optional)**

## Topics

### Providing an Introduction
- [@Intro(title: String)](./intro.md)
  Displays an introduction section at the top of a table of contents or tutorial page.
### Customizing Page Layout
- [@ContentAndMedia](./contentandmedia.md)
  Displays a grouping that contains text and an image or a video in a section on a tutorial page.
- [@Stack](./stack.md)
  Displays set of horizontally arranged groupings that contain text and media in a section on a tutorial page.
### Displaying Images
- [@Image(source: ResourceReference, alt: String)](./image.md)
  Displays an image in a tutorial.
### Testing Reader Knowledge
- [@Assessments](./assessments.md)
  Tests the reader’s knowledge at the end of a tutorial page.

## See Also

### Adding Tutorial Pages
- [@Tutorial(time: Int, projectFiles: ResourceReference)](./tutorial.md)
  Displays a tutorial page that teaches your Swift framework or package APIs through interactive coding exercises.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/article)*