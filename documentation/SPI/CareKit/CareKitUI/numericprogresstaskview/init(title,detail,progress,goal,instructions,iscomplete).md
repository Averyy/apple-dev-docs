---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/numericprogresstaskview/init(title:detail:progress:goal:instructions:iscomplete:)"
framework: "CareKit/CareKitUI"
---

# init(title:detail:progress:goal:instructions:isComplete:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Create an instance.

## Declaration

```swift
@MainActor
init(title: Text, detail: Text? = nil, progress: Text, goal: Text, instructions: Text? = nil, isComplete: Bool)
```

Available when `Header` is `_NumericProgressTaskViewHeader`.

## Parameters

- `title`: Title to display in the header.
- `detail`: Detail to display in the header.
- `progress`: Progress towards a `goal`.
- `goal`: The desired goal.
- `instructions`: Longer text displayed in the content of the view.
- `isComplete`: True if the view denotes the completed state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/numericprogresstaskview/init(title:detail:progress:goal:instructions:iscomplete:))*