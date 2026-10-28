---
url: "https://docs.swift.org/latest/documentation/docc/contentandmedia"
framework: "Swift-Org/docc"
---

# ContentAndMedia

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a grouping that contains text and an image or a video in a section on a tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@ContentAndMedia {
    ...
}
```

## Overview

Use a `ContentAndMedia` directive within a [`Section`](./section.md) or [`Stack`](./stack.md) directive to display a grouping that contains text and an image or a video. Set the `layout` parameter’s value to `"horizontal"`. Then, provide one or more paragraphs of text, followed by an [`Image`](./image.md) or [`Video`](./video.md) directive.

```markdown
@Tutorial(time: 30) {
    
    ...
    
    @Section(title: "Add a customization view") {
        @ContentAndMedia {
            Add the ability for users to customize sloths and select their powers.
            
            @Image(source: 01-creating-section2.png, alt: "An outline of a sloth surrounded by four power type icons. The power type icons are arranged in the following order, clockwise from the top: fire, wind, lightning, and ice.")
        }
            
        ...
 
    }
}
```

### Contained Elements

A content and media element must contain one of the following items:

- **[`Image`](./image.md)**: An image to display. **(optional)**
- **[`Video`](./video.md)**: A video to display. **(optional)**

### Containing Elements

The following items can include a content and media element:

- [`Section`](./section.md)
- [`Stack`](./stack.md)

## Topics

### Displaying Media
- [@Image(source: ResourceReference, alt: String)](./image.md)
  Displays an image in a tutorial.
- [@Video(source: ResourceReference, alt: String, poster: ResourceReference)](./video.md)
  Displays a video in a tutorial.

## See Also

### Customizing Page Layout
- [@Stack](./stack.md)
  Displays set of horizontally arranged groupings that contain text and media in a section on a tutorial page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/contentandmedia)*