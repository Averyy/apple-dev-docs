---
url: "https://docs.swift.org/latest/documentation/docc/stack"
framework: "Swift-Org/docc"
---

# Stack

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays set of horizontally arranged groupings that contain text and media in a section on a tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Stack {
    @ContentAndMedia { ... }
}
```

## Overview

Use the Stack directive to horizontally arrange between one and three groupings of text and media (images or videos) in a section on a tutorial page.

```markdown
@Tutorial(time: 30) {
    
    ...
    
    @Section(title: "Add a customization view") {
        @ContentAndMedia {
            Add the ability for users to customize sloths and select their powers.
            
            @Image(source: 01-creating-section2.png, alt: "An outline of a sloth surrounded by four power type icons. The power type icons are arranged in the following order, clockwise from the top: fire, wind, lightning, and ice.")
        }
        
        @Stack {
            @ContentAndMedia {
                ...
            }

            @ContentAndMedia {            
                ...            
            }

            @ContentAndMedia {
                ...
            }
        
        }            
        ...
 
    }
}
```

Example of a 1-column stack:

![A screenshot showing an example of a 1-column stack.](https://docs.swift.org/latest/images/org.swift.docc/tutorial-stack-1col@2x.png)

Example of a 2-column stack:

![A screenshot showing an example of a 2-column stack.](https://docs.swift.org/latest/images/org.swift.docc/tutorial-stack-2col@2x.png)

Example of a 3-column stack:

![A screenshot showing an example of a 3-column stack.](https://docs.swift.org/latest/images/org.swift.docc/tutorial-stack-3col@2x.png)

### Contained Elements

A stack contains the following items:

- **[`ContentAndMedia`](./contentandmedia.md)**: A grouping containing text and an image or a video. At least one is required `ContentAndMedia` element is required. **(optional)**

### Containing Elements

The following items can include a stack:

- [`Section`](./section.md)

## Topics

### Optional Directives
- [@ContentAndMedia](./contentandmedia.md)
  Displays a grouping that contains text and an image or a video in a section on a tutorial page.

## See Also

### Customizing Page Layout
- [@ContentAndMedia](./contentandmedia.md)
  Displays a grouping that contains text and an image or a video in a section on a tutorial page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/stack)*