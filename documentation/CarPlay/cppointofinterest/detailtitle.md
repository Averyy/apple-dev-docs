# detailTitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The detail card’s title.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var detailTitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * detailTitle;
```

#### Discussion

The template only displays the detail card when a user selects a point of interest. If this property is [`nil`](../../ObjectiveC/nil-227m0.md), the card displays the point of interest’s [`title`](./title.md) instead.

## See Also

### Managing the Detail Card’s Data
- [var detailSubtitle: String?](./detailsubtitle.md)
  The detail card’s subtitle.
- [var detailSummary: String?](./detailsummary.md)
  The detail card’s summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/detailtitle)*