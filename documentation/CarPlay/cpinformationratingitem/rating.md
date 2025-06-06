# rating

**Framework**: CarPlay  
**Kind**: property

The current rating that the template displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var rating: NSNumber? { get }
```

#### Discussion

This property is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) that contains a value in the range of 0 to [`maximumRating`](cpinformationratingitem/maximumrating.md). The value is an increment of 0.5.

## See Also

- [var maximumRating: NSNumber?](cpinformationratingitem/maximumrating.md)
  The maximum rating that the template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationratingitem/rating)*