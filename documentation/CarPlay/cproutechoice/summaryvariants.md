# summaryVariants

**Framework**: CarPlay  
**Kind**: property

An array of summary variants.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var summaryVariants: [String] { get }
```

#### Discussion

When creating the [`CPRouteChoice`](cproutechoice.md) object, localize each variant for display to the user. The system displays the first variant that fits into the available screen space, so arrange the variants from most to least preferred display order. The array contains at least one variant.

An example variant summary is 

## See Also

- [var additionalInformationVariants: [String]?](cproutechoice/additionalinformationvariants.md)
  An array of variants providing additional information about the route choice.
- [var selectionSummaryVariants: [String]?](cproutechoice/selectionsummaryvariants.md)
  An array of selection summary variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice/summaryvariants)*