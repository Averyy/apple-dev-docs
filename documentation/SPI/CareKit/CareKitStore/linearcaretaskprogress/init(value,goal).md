---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/linearcaretaskprogress/init(value:goal:)"
framework: "CareKit/CareKitStore"
---

# init(value:goal:)

**Framework**: CareKit/CareKitStore  
**Kind**: init  
**Role**: Initializer

Create a structure that defines user progress for a task that can be completed over time.

## Declaration

```swift
init(value: Double, goal: Double? = nil)
```

## Parameters

- `value`: The progress that’s been made towards reaching the goal.
- `goal`: A value that indicates whether the task is complete. When there is no goal, the value is `nil`. The task is considered completed if the progress value is greater than zero.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/linearcaretaskprogress/init(value:goal:))*