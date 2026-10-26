---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcome/init(taskuuid:taskoccurrenceindex:values:)"
framework: "CareKit/CareKitStore"
---

# init(taskUUID:taskOccurrenceIndex:values:)

**Framework**: CareKit/CareKitStore  
**Kind**: init  
**Role**: Initializer

Initialize by specifying the version of the task that owns this outcome, how many events have occurred before this outcome, and the values.

## Declaration

```swift
init(taskUUID: UUID, taskOccurrenceIndex: Int, values: [OCKOutcomeValue])
```

## Parameters

- `taskUUID`: The UUID of the task that owns this outcome. This ID can be retrieved from any task that has been queried from the store.
- `taskOccurrenceIndex`: The number of events that occurred before the event that owns this outcome.
- `values`: An array outcome values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcome/init(taskuuid:taskoccurrenceindex:values:))*