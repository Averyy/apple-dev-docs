# init(summaryVariants:additionalInformationVariants:selectionSummaryVariants:travelEstimates:)

**Framework**: CarPlay  
**Kind**: init

Initialize a @c CPRouteChoice with summary variants, additional information variants, selection summary variants, and travel estimates.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(summaryVariants: [String], additionalInformationVariants: [String], selectionSummaryVariants: [String], travelEstimates: CPTravelEstimates?)
```

#### Return Value

A new @c CPRouteChoice instance with travel estimates

#### Discussion

This initializer enables you to provide comprehensive route information including supplementary details through the travel estimates parameter. During route selection, users can compare routes based on time, distance, and additional factors like toll costs or energy consumption.

> **Note**: When travel estimates include additional route information, the system displays this information prominently during route selection to facilitate informed decision-making.

## Parameters

- `summaryVariants`: An array of summary strings, from most to least preferred. The system selects the first variant that fits available space. Example: “Via I-280 S”
- `additionalInformationVariants`: An array of additional information strings describing route characteristics. Example: “Fastest Route”, “Avoids Tolls”
- `selectionSummaryVariants`: An array of summary strings used when this route is selected
- `travelEstimates`: Optional travel estimates including distance, time, and additional route information like tolls, fuel consumption, or battery usage. This information helps users compare routes beyond just time and distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice/init(summaryvariants:additionalinformationvariants:selectionsummaryvariants:travelestimates:))*