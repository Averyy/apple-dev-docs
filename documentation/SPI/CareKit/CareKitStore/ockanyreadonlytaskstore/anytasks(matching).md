---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/anytasks(matching:)"
framework: "CareKit/CareKitStore"
---

# anyTasks(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of tasks that exist in the store.

## Declaration

```swift
func anyTasks(matching query: OCKTaskQuery) -> CareStoreQueryResults<OCKAnyTask>
```

#### Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that matches tasks in the store. If the query doesn’t contain a date interval, the result contains every version of a task. Multiple versions of the same task have the same [`id`](../ockanytask/id.md) but a different UUID. If the query does contain a date interval, the result contains the newest version of a task that exists in the interval.

## Parameters

- `query`: A query that matches tasks in the store.

## Default Implementations

### OCKAnyReadOnlyTaskStore Implementations
- [func anyTasks(matching: OCKTaskQuery) -> CareStoreQueryResults<OCKAnyTask>](./anytasks%28matching%29-9ni9s.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/anytasks(matching:))*