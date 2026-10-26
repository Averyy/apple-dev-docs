---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskviewcontroller/init(query:store:viewsynchronizer:modifytaskevents:)"
framework: "CareKit/CareKit"
---

# init(query:store:viewSynchronizer:modifyTaskEvents:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a view controller that displays a task view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
init(query: OCKEventQuery, store: OCKAnyStoreProtocol, viewSynchronizer: ViewSynchronizer, modifyTaskEvents: @escaping (OCKTaskEvents) -> OCKTaskEvents = { $0 })
```

## Parameters

- `query`: The query for fetching the task data to display.
- `store`: Contains the task data to display.
- `viewSynchronizer`: Capable of creating and updating the view using the task data.
- `modifyTaskEvents`: Modify task events before they are applied to the view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskviewcontroller/init(query:store:viewsynchronizer:modifytaskevents:))*