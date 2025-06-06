# additionalInformationVariants

**Framework**: CarPlay  
**Kind**: property

An array of variants providing additional information about the route choice.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var additionalInformationVariants: [String]? { get }
```

#### Discussion

When creating a [`CPRouteChoice`](cproutechoice.md) object, localize each variant for display to the user. The system displays the first variant that fits into the available screen space, so arrange the variants from most to least preferred display order. The array contains at least one variant.

Examples of additional information variants include  and .

## See Also

- [var summaryVariants: [String]](cproutechoice/summaryvariants.md)
  An array of summary variants.
- [var selectionSummaryVariants: [String]?](cproutechoice/selectionsummaryvariants.md)
  An array of selection summary variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice/additionalinformationvariants)*