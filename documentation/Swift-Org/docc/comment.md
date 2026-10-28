---
url: "https://docs.swift.org/latest/documentation/docc/comment"
framework: "Swift-Org/docc"
---

# Comment

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Captures a writer comment that’s not visible in the rendered documentation.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Comment {
    ...
}
```

## Overview

Use a comment directive to include author notes, like reminders to add more content, in your reference documentation or tutorial. DocC ignores comments when your documentation builds, and they don’t appear in the rendered content.

```markdown
@Comment {
    Add lots more photos of sloths here!
} 
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/comment)*