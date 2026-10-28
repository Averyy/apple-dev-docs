# additionalInformationVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of variants providing additional information about the route choice.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var additionalInformationVariants: [String]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * additionalInformationVariants;
```

## Discussion

When creating a [`CPRouteChoice`](../cproutechoice.md) object, localize each variant for display to the user. The system displays the first variant that fits into the available screen space, so arrange the variants from most to least preferred display order. The array contains at least one variant.

Examples of additional information variants include *Fastest Route* and *Avoids Tolls*.

## See Also

### Getting Variants
- [var summaryVariants: [String]](./summaryvariants.md)
  An array of summary variants.
- [var selectionSummaryVariants: [String]?](./selectionsummaryvariants.md)
  An array of selection summary variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice/additionalinformationvariants)*