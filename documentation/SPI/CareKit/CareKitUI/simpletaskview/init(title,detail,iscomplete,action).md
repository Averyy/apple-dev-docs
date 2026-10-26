---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/simpletaskview/init(title:detail:iscomplete:action:)"
framework: "CareKit/CareKitUI"
---

# init(title:detail:isComplete:action:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Create an instance.

## Declaration

```swift
@MainActor
init(title: Text, detail: Text? = nil, isComplete: Bool, action: @escaping () -> Void = {})
```

Available when `Header` is `_SimpleTaskViewHeader`.

## Parameters

- `title`: The title to display in the header.
- `detail`: The detail to display in the header.
- `isComplete`: True if the view denotes the completed state.
- `action`: The action to perform when the whole view is tapped.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/simpletaskview/init(title:detail:iscomplete:action:))*