---
url: "https://docs.swift.org/latest/documentation/docc/chapter"
framework: "Swift-Org/docc"
---

# Chapter

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Organizes related tutorial pages into a chapter on a table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Chapter(name: String) {
    ...

    @Image(source: ResourceReference, alt: String?) { ... }
    @TutorialReference(tutorial: TopicReference)
}
```

## Mentions

- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)

#### Overview

Chapters appear on a table of contents page and help provide a sense of context and accomplishment as readers move through your tutorial content.

![A screenshot showing a chapter on a table of contents page.](https://docs.swift.org/latest/images/org.swift.docc/tutorial-chapter@2x.png)

Use `Chapter` directives to organize related tutorial pages into groupings. For each chapter, use the `name` parameter to specify a chapter name, and provide some descriptive text. Then, insert [`TutorialReference`](./tutorialreference.md) directives for the tutorial pages each chapter contains. Optionally, use [`Image`](./image.md) directives to show images that illustrate the chapters’ content.

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Chapter(name: "SlothCreator Essentials") {
        @Image(source: chapter1-slothcreatorEssentials, alt: "A wireframe of an app interface that has an outline of a sloth and four buttons below the sloth. The buttons display the following symbols, from left to right: snowflake, fire, wind, and lightning.")
        
        Create custom sloths and edit their attributes and powers using SlothCreator.
        
        @TutorialReference(tutorial: "doc:Creating-Custom-Sloths")
    }

    ...
    
}
```

##### Group Related Chapters

If you need a second level of organization on a table of contents page, use [`Volume`](./volume.md) directives to organize related chapters into volume groupings.

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

##### Contained Elements

A chapter can contain the following items:

- **[`Image`](./image.md)**: An image that represents the chapter’s content. **(optional)**
- **[`TutorialReference`](./tutorialreference.md)**: A reference to a tutorial page. A chapter must contain at least one tutorial page reference. **(optional)**

##### Containing Elements

The following items can contain chapters:

- [`Tutorials`](./tutorials.md)
- [`Volume`](./volume.md)

## Parameters

- `name`: The name of the chapter. **(required)**

## Topics

### Referencing Tutorials
- [@TutorialReference(tutorial: TopicReference)](./tutorialreference.md)
  Adds an individual tutorial page link to a chapter on a table of contents page.
### Displaying an Image
- [@Image(source: ResourceReference, alt: String)](./image.md)
  Displays an image in a tutorial.

## See Also

### Organizing Content
- [@Volume(...)](./volume.md)
  Organizes related chapters into a volume on a tutorial’s table of contents page.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/chapter)*