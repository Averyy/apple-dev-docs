---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewcontroller/init(plottype:selecteddate:configurations:store:)"
framework: "CareKit/CareKit"
---

# init(plotType:selectedDate:configurations:store:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a view controller that displays a chart view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
init(plotType: OCKCartesianGraphView.PlotType, selectedDate: Date, configurations: [OCKDataSeriesConfiguration], store: OCKAnyStoreProtocol)
```

## Parameters

- `plotType`: The type of plot that is displayed in the view.
- `selectedDate`: The currently selected date in the chart.
- `configurations`: Specifies which data to query and how to display it on the graph.
- `store`: Contains the task data to display.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewcontroller/init(plottype:selecteddate:configurations:store:))*