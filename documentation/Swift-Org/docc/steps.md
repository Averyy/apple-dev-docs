---
url: "https://docs.swift.org/latest/documentation/docc/steps"
framework: "Swift-Org/docc"
---

# Steps

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Defines a set of tasks the reader performs on a tutorial page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Steps {
    ...
}
```

## Mentions

- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)

## Overview

Use the `Steps` directive to define a set of tasks the reader performs on a tutorial page.

![A screenshot showing three steps on a tutorial page.](https://docs.swift.org/latest/images/org.swift.docc/3@2x.png)

Each individual step contains instructional text along with either a code listing, an image , or a video.

```markdown
@Tutorial(time: 30) {
    
    ...
    
    @Section(title: "Create a Swift Package") {
        @ContentAndMedia {

            ...

        }
        
        @Steps {
            @Step {
                Create a new directory named `SwiftPackage`.
                
                @Code(name: "CreateDirectory.sh", file: 01-create-dir.sh) {
                    @Image(source: preview-01-create-directory.png, alt: "A screenshot from the command-line showing creating the directory using the `mkdir SwiftPackage` command.")
                }
            }    

        @Step {
            Change into the new directory.
            
            @Code(name: "ChangeDirectory.sh", file: 02-change-directory.sh) {
                @Image(source: preview-02-change-directory.png, alt: "A screenshot from the command-line showing changing into the directory using the `cd SwiftPackage` command.")
            }
        }    

            @Step {
                Create a new Swift Package.
                
                @Code(name: "Package.swift", file: 03-create-package.sh) {
                    @Image(source: preview-03-create-package.png, alt: "A screenshot from the command-line showing Swift Package creation using the `swift package init` command.")
                }
            }    
            
            ...

        }
    }
}
```

### Contained Elements

A set of steps can contain one or more of the following items:

- **[`Step`](./step.md)**: An individual task the reader performs. **(optional)**

### Containing Elements

The following items can include a set of steps:

- [`Section`](./section.md)

## Topics

### Adding Individual Steps
- [@Step](./step.md)
  Defines an individual task the reader performs within a set of steps on a tutorial page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/steps)*