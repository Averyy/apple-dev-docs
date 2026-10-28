---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/fetchanytask(withid:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyTask(withID:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Asynchronously retrieve an array of tasks from the store using its user-defined unique identifier.

## Declaration

```swift
func fetchAnyTask(withID id: String) async throws -> OCKAnyTask
```

## Discussion

If a task with the specified identifier isn’t found, the completion handler receives an error.

## Parameters

- `id`: The identifier of the item to fetch.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/fetchanytask(withid:))*