---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/instructionstaskview/init(title:detail:instructions:iscomplete:action:)"
framework: "CareKit/CareKitUI"
---

# init(title:detail:instructions:isComplete:action:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Create an instance.

## Declaration

```swift
@MainActor
init(title: Text, detail: Text? = nil, instructions: Text? = nil, isComplete: Bool, action: @escaping () -> Void)
```

Available when `Header` is `_InstructionsTaskViewHeader`.

## Parameters

- `title`: Title to display in the header.
- `detail`: Detail to display in the header.
- `instructions`: Longer text displayed in the content of the view.
- `isComplete`: True if the view denotes the completed state.
- `action`: Action to perform when the completion button is tapped.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/instructionstaskview/init(title:detail:instructions:iscomplete:action:))*