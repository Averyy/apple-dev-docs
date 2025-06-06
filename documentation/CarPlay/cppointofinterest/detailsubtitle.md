# detailSubtitle

**Framework**: CarPlay  
**Kind**: property

The detail card’s subtitle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var detailSubtitle: String? { get set }
```

#### Discussion

The template only displays a detail card when the user selects a point of interest. If this property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0), the card displays the point of interest’s [`subtitle`](cppointofinterest/subtitle.md) instead.

## See Also

- [var detailTitle: String?](cppointofinterest/detailtitle.md)
  The detail card’s title.
- [var detailSummary: String?](cppointofinterest/detailsummary.md)
  The detail card’s summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/detailsubtitle)*