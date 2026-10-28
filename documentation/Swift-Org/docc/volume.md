---
url: "https://docs.swift.org/latest/documentation/docc/volume"
framework: "Swift-Org/docc"
---

# Volume

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Organizes related chapters into a volume on a tutorial’s table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Volume(...) {
    ...
}
```

## Overview

If you need a second level of organization on a table of contents page, use `Volume` directives to organize related chapters into volume groupings. For each volume, use the `name` parameter to specify a volume name, and provide some descriptive text. Then, insert [`Chapter`](./chapter.md) directives for the chapters each volume contains. Optionally, use an [`Image`](./image.md) directive to show an image for a volume.

```markdown
@Tutorials(name: "SlothCreator") {
    @Intro(title: "Meet SlothCreator") {
        
        ...
    }
    
    @Volume(name: "Getting Started") {
        Building sloths, caring for them, and interacting with them.
        
        @Chapter(name: "SlothCreator Essentials") {
            ...
        }
        
        @Chapter(name: "Basic Sloth Care") {
            ...
        }
        
        @Chapter(name: "Basic Sloth Interaction") {
            ...
        }
    }
    
    @Volume(name: "Climbing Higher") {
        Taking your sloths to the next level.
        
        @Chapter(name: "Powering Up") {
            ...
        }
    
        ...
    }
    
   ...
}
```

### Contained Elements

A volume can contain the following items:

- **[`Chapter`](./chapter.md)**: A chapter containing one or more tutorial pages. A volume must contain at least one chapter. **(optional)**
- **[`Image`](./image.md)**: An image that represents the volume’s content. **(optional)**

### Containing Elements

The following pages can include volumes:

- [`Tutorials`](./tutorials.md)

## Parameters

- `name`: The name of the volume. **(required)**

## Topics

### Referencing Chapters
- [@Chapter(name: String)](./chapter.md)
  Organizes related tutorial pages into a chapter on a table of contents page.
### Displaying an Image
- [@Image(source: ResourceReference, alt: String)](./image.md)
  Displays an image in a tutorial.

## See Also

### Organizing Content
- [@Chapter(name: String)](./chapter.md)
  Organizes related tutorial pages into a chapter on a table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/volume)*