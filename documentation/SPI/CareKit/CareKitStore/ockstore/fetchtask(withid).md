---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchtask(withid:)"
framework: "CareKit/CareKitStore"
---

# fetchTask(withID:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`fetchTask` asynchronously retrieves an array of tasks from the store using its user-defined unique identifier. If a task with the specified identifier is not found, the completion handler will be called with an error.

## Declaration

```swift
func fetchTask(withID id: String) async throws -> Task
```

## Parameters

- `id`: The identifier of the item to be fetched.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchtask(withid:))*