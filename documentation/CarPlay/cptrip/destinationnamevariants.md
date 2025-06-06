# destinationNameVariants

**Framework**: CarPlay  
**Kind**: property

An array of strings that represents the names of the destination for this trip, arranged from most to least preferred.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var destinationNameVariants: [String]? { get set }
```

#### Discussion

You need to provide at least one variant. Present the variant strings as localized, displayable content.

## See Also

- [var routeChoices: [CPRouteChoice]](cptrip/routechoices.md)
  The list of route choices for the trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip/destinationnamevariants)*