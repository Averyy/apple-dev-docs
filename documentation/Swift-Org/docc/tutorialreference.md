---
url: "https://docs.swift.org/latest/documentation/docc/tutorialreference"
framework: "Swift-Org/docc"
---

# TutorialReference

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Adds an individual tutorial page link to a chapter on a table of contents page.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@TutorialReference(tutorial: TopicReference)
```

## Overview

Use the `TutorialReference` directive in a chapter on a table of contents page to link to a specific tutorial page. Include one `TutorialReference` per chapter. For each, use the `tutorial` parameter to reference the page by name, preceded by the doc: prefix.

```markdown
@Tutorials(name: "SlothCreator") {
    
    ...
    
    @Chapter(name: "SlothCreator Essentials") {
        @Image(source: chapter1-slothcreatorEssentials.png, alt: "A wireframe of an app interface that has an outline of a sloth and four buttons below the sloth. The buttons display the following symbols, from left to right: snowflake, fire, wind, and lightning.")
        
        Create custom sloths and edit their attributes and powers using SlothCreator.
        
        @TutorialReference(tutorial: "doc:Creating-Custom-Sloths")
    }

    ...
    
}
```

### Containing Elements

The following items can include tutorial page references:

- [`Chapter`](./chapter.md)

## Parameters

- `tutorial`: A link to a tutorial page, in the format *`<doc:[TutorialPageFileName]>`*. For example, *`<doc:Creating-Custom-Sloths>`*.  **(required)**


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/tutorialreference)*