---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/instructionstaskview/init(instructions:iscomplete:action:header:)"
framework: "CareKit/CareKitUI"
---

# init(instructions:isComplete:action:header:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Create an instance.

## Declaration

```swift
@MainActor
init(instructions: Text? = nil, isComplete: Bool, action: @escaping () -> Void, @ViewBuilder header: () -> Header)
```

## Parameters

- `instructions`: Instructions text
- `isComplete`: True if the view denotes the completed state.
- `action`: Action to perform when the completion button is tapped.
- `header`: Injected at the top of the view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/instructionstaskview/init(instructions:iscomplete:action:header:))*