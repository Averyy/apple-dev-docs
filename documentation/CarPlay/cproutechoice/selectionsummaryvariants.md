# selectionSummaryVariants

**Framework**: CarPlay  
**Kind**: property

An array of selection summary variants.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var selectionSummaryVariants: [String]? { get }
```

#### Discussion

When creating a [`CPRouteChoice`](cproutechoice.md) object, localize each variant for display to the user. The system displays the first variant that fits in the available screen space, so arrange the variants from most to least preferred display order. The array contains at least one variant.

## See Also

- [var summaryVariants: [String]](cproutechoice/summaryvariants.md)
  An array of summary variants.
- [var additionalInformationVariants: [String]?](cproutechoice/additionalinformationvariants.md)
  An array of variants providing additional information about the route choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice/selectionsummaryvariants)*