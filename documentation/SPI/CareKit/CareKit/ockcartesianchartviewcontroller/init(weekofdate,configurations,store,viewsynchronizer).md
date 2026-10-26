---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewcontroller/init(weekofdate:configurations:store:viewsynchronizer:)"
framework: "CareKit/CareKit"
---

# init(weekOfDate:configurations:store:viewSynchronizer:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a view controller that displays a chart view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
override init(weekOfDate: Date, configurations: [OCKDataSeriesConfiguration], store: OCKAnyStoreProtocol, viewSynchronizer: OCKCartesianChartViewSynchronizer)
```

## Parameters

- `weekOfDate`: A date in the week of the insights range to fetch.
- `configurations`: Specifies which data to query and how it to display in on the graph.
- `store`: Contains the task data that will be displayed.
- `viewSynchronizer`: Capable of creating and updating the view using the data series.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewcontroller/init(weekofdate:configurations:store:viewsynchronizer:))*