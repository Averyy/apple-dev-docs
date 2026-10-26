---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockchartviewcontroller/init(weekofdate:configurations:store:viewsynchronizer:)"
framework: "CareKit/CareKit"
---

# init(weekOfDate:configurations:store:viewSynchronizer:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

A view controller that displays a chart view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
init(weekOfDate: Date, configurations: [OCKDataSeriesConfiguration], store: OCKAnyStoreProtocol, viewSynchronizer: ViewSynchronizer)
```

## Parameters

- `weekOfDate`: A date in the week of the insights range to fetch.
- `configurations`: Specifies which data should be queried and how it should be displayed by the graph.
- `store`: Contains the task data that will be displayed.
- `viewSynchronizer`: Capable of creating and updating the view using the data series.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockchartviewcontroller/init(weekofdate:configurations:store:viewsynchronizer:))*