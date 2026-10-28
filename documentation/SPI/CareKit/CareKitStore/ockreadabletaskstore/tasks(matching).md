---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/tasks(matching:)"
framework: "CareKit/CareKitStore"
---

# tasks(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of tasks that exist in the store.

## Declaration

```swift
func tasks(matching query: OCKTaskQuery) -> Tasks
```

## Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match tasks in the store. If the query doesn’t contain a date interval, the result will contain every version of a task. Multiple versions of the same task will have the same [`id`](../ockanytask/id.md) but a different UUID. If the query does contain a date interval, the result will contain the newest version of a task that exists in the interval.

## Parameters

- `query`: Used to match tasks in the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/tasks(matching:))*