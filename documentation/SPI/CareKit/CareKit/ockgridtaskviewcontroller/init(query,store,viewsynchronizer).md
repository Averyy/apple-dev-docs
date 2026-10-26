---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockgridtaskviewcontroller/init(query:store:viewsynchronizer:)"
framework: "CareKit/CareKit"
---

# init(query:store:viewSynchronizer:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a view controller that displays a task view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
init(query: OCKEventQuery, store: OCKAnyStoreProtocol, viewSynchronizer: OCKGridTaskViewSynchronizer = OCKGridTaskViewSynchronizer())
```

## Parameters

- `query`: Fetches the task data to display.
- `store`: Contains the task data to display.
- `viewSynchronizer`: Capable of creating and updating the view using the task data.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockgridtaskviewcontroller/init(query:store:viewsynchronizer:))*