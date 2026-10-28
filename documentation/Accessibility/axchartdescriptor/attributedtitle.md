# attributedTitle

**Framework**: Accessibility  
**Kind**: property  
**Role**: Instance Property

An attributed version of the chart title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@NSCopying
var attributedTitle: NSAttributedString? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedTitle;
```

## Discussion

If you set the value of this property, the system uses this value instead of [`title`](./title.md).

## See Also

### Specifying the chart title
- [var title: String?](./title.md)
  The title of the chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axchartdescriptor/attributedtitle)*