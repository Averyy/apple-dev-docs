---
url: "https://docs.swift.org/latest/documentation/docc/tab"
framework: "Swift-Org/docc"
---

# Tab

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A container directive that holds general markup content describing an individual tab within a tab-based layout.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@Tab(_ title: String) {
    ...
}
```

#### Overview

To add a new tab to a [`TabNavigator`](./tabnavigator.md), add a `@Tab` directive within the content of the `@TabNavigator` directive.

## Parameters

- `title`: The title that should identify the content in this tab when rendered. **(required)**


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/tab)*