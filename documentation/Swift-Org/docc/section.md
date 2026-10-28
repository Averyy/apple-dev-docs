---
url: "https://docs.swift.org/latest/documentation/docc/section"
framework: "Swift-Org/docc"
---

# Section

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a grouping of text, images, and tasks on a tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Section(...) {
    ...
}
```

## Mentions

- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)

## Overview

Use a `Section` directive to show a unit of work that consists of text, media (for example images and videos), and tasks on a tutorial page. A tutorial page must includes one or more sections.

![A screenshot showing a section on a tutorial page. The section includes text, an image, and coding steps.](https://docs.swift.org/latest/images/org.swift.docc/1@2x.png)

Use the `title` parameter to provide a name for the section. Then, use the [`ContentAndMedia`](./contentandmedia.md) directive to add text and media that introduces the tasks that the reader needs to follow. This directive must be the first directive in the section. You can optionally show additional text and media by inserting a [`Stack`](./stack.md) directive. A stack contains between one and three horizontally arranged `ContentAndMedia` directives. Finally, add a [`Steps`](./steps.md) directive to insert a set of tasks for the reader to perform.

```markdown
@Tutorial(time: 30) {
    
    ...
    
    @Section(title: "Add a customization view") {
        @ContentAndMedia {
            Add the ability for users to customize sloths and select their powers.
            
            @Image(source: 01-creating-section2.png, alt: "An outline of a sloth surrounded by four power type icons. The power type icons are arranged in the following order, clockwise from the top: fire, wind, lightning, and ice.")
        }
        
        @Steps {
            @Step {
                Create a new SwiftUI View file named `CustomizedSlothView.swift`.
                
                @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-01.swift) {
                    @Image(source: preview-01-creating-code-02-01.png, alt: "A screenshot as it would appear on iPhone, with the text, Hello, World!, centered in the middle of the display.")
                }
            }    
            
            @Step {
                
                ...
                
            }    
            
            ...
 
        }
    }
}
```

### Contained Elements

A section can contain the following items:

- **[`ContentAndMedia`](./contentandmedia.md)**: A grouping that contains text and an image or video. At least one `ContentAndMedia` directive is required and must be the first element within a section. **(optional)**
- **[`Stack`](./stack.md)**: A set of horizontally arranged groupings of text and media. **(optional)**
- **[`Steps`](./steps.md)**: A set of tasks the reader performs. **(optional)**

### Containing Elements

The following pages can include sections:

- [`Tutorial`](./tutorial.md)

## Parameters

- `title`: The name of the section. **(required)**

## Topics

### Introducing a Section
- [@ContentAndMedia](./contentandmedia.md)
  Displays a grouping that contains text and an image or a video in a section on a tutorial page.
### Displaying Tasks
- [@Steps](./steps.md)
  Defines a set of tasks the reader performs on a tutorial page.
### Arranging Content and Media
- [@Stack](./stack.md)
  Displays set of horizontally arranged groupings that contain text and media in a section on a tutorial page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/section)*