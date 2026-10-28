# detailSummary

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The detail card’s summary.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var detailSummary: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * detailSummary;
```

## Discussion

The template only displays a detail card when the user selects a point of interest. If this property is [`nil`](../../ObjectiveC/nil-227m0.md), the card displays the point of interest’s [`summary`](./summary.md) instead.

## See Also

### Managing the Detail Card’s Data
- [var detailTitle: String?](./detailtitle.md)
  The detail card’s title.
- [var detailSubtitle: String?](./detailsubtitle.md)
  The detail card’s subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/detailsummary)*