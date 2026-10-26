---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/numericprogresstaskview/init(progress:goal:instructions:iscomplete:header:)"
framework: "CareKit/CareKitUI"
---

# init(progress:goal:instructions:isComplete:header:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Create an instance.

## Declaration

```swift
@MainActor
init(progress: Text, goal: Text, instructions: Text? = nil, isComplete: Bool, @ViewBuilder header: () -> Header)
```

## Parameters

- `progress`: Progress towards a `goal`.
- `goal`: The desired goal.
- `instructions`: Longer text displayed in the content of the view.
- `isComplete`: True if the view denotes the completed state.
- `header`: Injected at the top of the view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/numericprogresstaskview/init(progress:goal:instructions:iscomplete:header:))*