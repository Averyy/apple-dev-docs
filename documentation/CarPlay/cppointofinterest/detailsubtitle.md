# detailSubtitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The detail card’s subtitle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var detailSubtitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * detailSubtitle;
```

#### Discussion

The template only displays a detail card when the user selects a point of interest. If this property is [`nil`](../../ObjectiveC/nil-227m0.md), the card displays the point of interest’s [`subtitle`](./subtitle.md) instead.

## See Also

### Managing the Detail Card’s Data
- [var detailTitle: String?](./detailtitle.md)
  The detail card’s title.
- [var detailSummary: String?](./detailsummary.md)
  The detail card’s summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/detailsubtitle)*