# detailTitle

**Framework**: CarPlay  
**Kind**: property

The detail card’s title.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var detailTitle: String? { get set }
```

#### Discussion

The template only displays the detail card when a user selects a point of interest. If this property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0), the card displays the point of interest’s [`title`](cppointofinterest/title.md) instead.

## See Also

- [var detailSubtitle: String?](cppointofinterest/detailsubtitle.md)
  The detail card’s subtitle.
- [var detailSummary: String?](cppointofinterest/detailsummary.md)
  The detail card’s summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/detailtitle)*