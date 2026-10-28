---
url: "https://docs.swift.org/latest/documentation/docc/tutorial"
framework: "Swift-Org/docc"
---

# Tutorial

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays a tutorial page that teaches your Swift framework or package APIs through interactive coding exercises.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Tutorial(time: Int?, projectFiles: ResourceReference?) {
    @Intro(title: String) { ... }
    @Section(...) { ... }
}
```

## Mentions

- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)

## Overview

The `Tutorial` directive defines the structure of an individual tutorial page that teaches your Swift framework or package APIs through a series of interactive steps. Your tutorial can include one or more of these individual tutorial pages, and readers navigate to them from a table of contents page—defined by the [`Tutorials`](./tutorials.md) directive.

![A screenshot of the top portion of a tutorial page.](https://docs.swift.org/latest/images/org.swift.docc/tutorial-page@2x.png)

### Create the Tutorial File

Use a text editor to add a Tutorial file to your documentation catalog and ensure the filename ends in `.tutorial`. Copy and paste the template below into your editor.

```markdown
@Tutorial(time: <#number#>) {
    @Intro(title: "<#text#>") {
        <#text#>
        
        @Image(source: <#file#>, alt: "<#accessible description#>")
    }
    
    @Section(title: "<#text#>") {
        @ContentAndMedia {
            <#text#>
            
            @Image(source: <#file#>, alt: "<#accessible description#>")
        }
        
        @Steps {
            @Step {
                <#text#>
                @Image(source: <#file#>, alt: "<#accessible description#>")
            }
            
            @Step {
                <#text#>
                @Code(name: "<#display name#>", file: <#filename.swift#>)
            }
        }
    }
}
```

### Estimate Completion Time

You can give the reader an idea of how long the tutorial page might take to complete by providing an optional estimate in the `time` parameter. Completion time estimates help the reader understand how long they need to set aside to learn your APIs.

```markdown
@Tutorial(time: 30) {

    ...

}
```

When you provide estimates on your individual tutorial pages, the introduction section on the table of contents page automatically calculates and displays a total-completion time estimate for the entire tutorial.

### Provide Source Material

If you need to add downloadable materials, like sample projects and code examples, for your tutorials, archive them and add them to your documentation catalog. Consider offering a base project to which the reader can add code as they work through the steps, as well as a finished project for comparison with their work.

Project files can reside anywhere in your documentation catalog, but it’s good practice to centralize them in a Resources folder. You may want to create a tutorial-specific one if you created a tutorial folder in your documentation catalog.

To share project files with the reader, provide the archive’s name and extension in the `projectFiles` parameter.

```markdown
@Tutorial(time: 30, projectFiles: "SlothCreatorFiles.zip") {

    ...

}
```

### Add an Introduction

A tutorial page begins with an introduction section, defined by an [`Intro`](./intro.md) directive. The introduction is the first thing a reader sees on the page, so it needs to draw them into the content that follows and let them know what to expect. An introduction includes text and an image that serves as the section’s background, or a link to an introduction video.

```markdown
@Tutorial(time: 30) {
    @Intro(title: "Creating and Building a Swift Package") {
        This tutorial guides you through creating and building a Swift Package. Use the package to add your own re-usable classes and structures.
        
        @Image(source: creating-intro, alt: "An image of the Swift logo.")
    }

    ...
    
}
```

### Add Sections of Steps

A tutorial page includes sets of steps the reader performs, and those steps are organized into logical sections. For example, a tutorial might include a section of steps that guides a reader through setting up a Swift package, and another section that covers adding a class to that package.

Define sections using the [`Section`](./section.md) directive. You can optionally start with descriptive text and an image or video animation by using the [`ContentAndMedia`](./contentandmedia.md) directive. Once you define a section, you can include steps to perform coding tasks by using the [`Steps`](./steps.md) directive. See the [`Code`](./code.md) directive to learn how to provide code for a step.

```markdown
@Tutorial(time: 30) {
    @Intro(title: "Creating Custom Sloths") {
        
        ...

    }
    
    @Section(title: "Create a Swift Package in a new directory") {
        @ContentAndMedia {
            
            ...
            
        }
        
        @Steps {
            @Step {
                Create the directory.
                
                @Image(source: placeholder-image, alt: "A screenshot showing the command to type in the terminal to create the directory.")
            }
            
            @Step {
                Create the Swift Package. 
                
                @Image(source: placeholder-image, alt: "A screenshot showing the command to type in the terminal to create the Swift package.")
            }
            
            @Step {
                
                ...

            }
            
            @Step {

                ...

            }
        }
    }
    
    @Section(title: "Add a customization view") {
        @ContentAndMedia {

            ...

        }
        
        @Steps {
        
            ...

        }    
    }
}
```

### Check the Reader’s Knowledge

At the end of a tutorial page, you can optionally use an [`Assessments`](./assessments.md) directive to create a section that tests the reader’s knowledge. An assessment section includes a set of multiple-choice questions. If the reader gets a question wrong, you can provide a hint that points them toward the correct answer so they can try again.

```markdown
@Tutorial(time: 30) {
    @Intro(title: "Creating Custom Sloths") {
        
        ...

    }
    
    @Section(title: "Create a new project and add SlothCreator") {
        @ContentAndMedia {
            
            ...

        }
        
        @Steps {
            
            ...

        }
    }
    
    ...

    @Assessments {
        @MultipleChoice {
            What element did you use to add space around and between your views?

            @Choice(isCorrect: false) {
                A state variable.

                @Justification(reaction: "Try again!") {
                    Remember, it's something you used to arrange views vertically.
                }
            }

            @Choice(isCorrect: true) {
                A VStack with trailing padding.

                @Justification(reaction: "That's right!") {
                    A VStack arranges views in a vertical line.
                }
            }

            @Choice(isCorrect: false) {
              
              ...
              
            }
        }
    }
}
```

To see the creation of a simple tutorial project from start to finish, see [Building an Interactive Tutorial](./building-an-interactive-tutorial.md).

### Contained Elements

A tutorial page can contain the following items:

- **[`Intro`](./intro.md)**: Engaging introductory text and an image or video to display at the top of the page. **(required)**
- **[`Section`](./section.md)**: A group of related steps. **(required)**
- **[`Assessments`](./assessments.md)**: Assessments that test the reader’s knowledge about the steps performed on the page. **(optional)**
- **[`Image`](./image.md)**: An image that appears on the page. **(optional)**

## Parameters

- `time`: An integer value that represents the estimated time it takes to complete the tutorial, in minutes. **(optional)**
- `projectFiles`: The name and extension of an archive in your code base, which the reader can download and use or reference while following the tutorial’s steps. **(optional)**

## Topics

### Setting an Xcode Requirement
- [@XcodeRequirement(title: String, destination: URL)](./xcoderequirement.md)
  Lists the Xcode version required by a tutorial, and provides a link to download it.
### Providing an Introduction
- [@Intro(title: String)](./intro.md)
  Displays an introduction section at the top of a table of contents or tutorial page.
### Displaying Tasks
- [@Section(...)](./section.md)
  Displays a grouping of text, images, and tasks on a tutorial page.
### Displaying Images
- [@Image(source: ResourceReference, alt: String)](./image.md)
  Displays an image in a tutorial.
### Testing Reader Knowledge
- [@Assessments](./assessments.md)
  Tests the reader’s knowledge at the end of a tutorial page.

## See Also

### Related Documentation
- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)
  Construct a step-by-step guided learning experience for your Swift framework or package.
### Adding Tutorial Pages
- [@Article(...)](./article.md)
  Displays a tutorial article page that teaches a conceptual topic about your Swift framework or package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/tutorial)*