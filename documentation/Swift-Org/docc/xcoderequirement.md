---
url: "https://docs.swift.org/latest/documentation/docc/xcoderequirement"
framework: "Swift-Org/docc"
---

# XcodeRequirement

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Lists the Xcode version required by a tutorial, and provides a link to download it.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@XcodeRequirement(title: String, destination: URL)
```

## Overview

If a tutorial page (`Tutorial`) requires a specific version of Xcode in order for the reader to follow along, use the `XcodeRequirement` directive to denote the requirement and provide a download link.

```markdown
@Tutorial(time: 30) {
    @XcodeRequirement(
        title: "Xcode 13", 
        destination: "https://developer.apple.com/download/")
    
    ...

}
```

### Containing Elements

The following pages can display an Xcode requirement:

- [`Tutorial`](./tutorial.md)

## Parameters

- `title`: The Xcode name and version required by the tutorial. For example: “Xcode 13”. **(required)**
- `destination`: A URL to download the required version of Xcode. **(required)**


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/xcoderequirement)*