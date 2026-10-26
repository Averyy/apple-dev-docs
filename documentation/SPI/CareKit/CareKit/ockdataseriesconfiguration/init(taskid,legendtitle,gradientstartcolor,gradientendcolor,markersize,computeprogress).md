---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdataseriesconfiguration/init(taskid:legendtitle:gradientstartcolor:gradientendcolor:markersize:computeprogress:)"
framework: "CareKit/CareKit"
---

# init(taskID:legendTitle:gradientStartColor:gradientEndColor:markerSize:computeProgress:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Initialize a new `OCKDataSeriesConfiguration`.

## Declaration

```swift
init(taskID: String, legendTitle: String, gradientStartColor: UIColor, gradientEndColor: UIColor, markerSize: CGFloat, computeProgress: @escaping (OCKAnyEvent) -> LinearCareTaskProgress = { event in
            event.computeProgress(by: .summingOutcomeValues)
        })
```

## Parameters

- `taskID`: A user-provided unique id for a task.
- `legendTitle`: The title that will be used to represent this data series in the legend.
- `gradientStartColor`: The first of two colors that will be used in the gradient when plotting the data.
- `gradientEndColor`: The second of two colors that will be used in the gradient when plotting the data.
- `markerSize`: The marker size determines the size of the line, bar, or scatter plot elements. The precise behavior varies by plot type.
- `computeProgress`: Used to compute progress for an event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdataseriesconfiguration/init(taskid:legendtitle:gradientstartcolor:gradientendcolor:markersize:computeprogress:))*