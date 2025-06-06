# init(summaryVariants:additionalInformationVariants:selectionSummaryVariants:)

**Framework**: CarPlay  
**Kind**: init

Creates a route choice.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(summaryVariants: [String], additionalInformationVariants: [String], selectionSummaryVariants: [String])
```

#### Return Value

A newly initialized route choice.

## Parameters

- `summaryVariants`: An array of summary variants. The system displays the first variant that fits in the available screen space, so arrange the variants from most to least preferred display order. You should localize each variant for display to the user. You must provide at least one variant; for example,  .
- `additionalInformationVariants`: An array of variants providing additional information about the route choice. The system displays the first variant that fits in the available screen space, so arrange the variants from most to least preferred display order. You should localize each variant for display to the user. You must provide at least one variant; for example,   or  .
- `selectionSummaryVariants`: An array of selection summary variants. The system displays the first variant that fits in the available screen space, so arrange the variants from most to least preferred display order. You should localize each variant for display to the user. You must provide at least one variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice/init(summaryvariants:additionalinformationvariants:selectionsummaryvariants:))*