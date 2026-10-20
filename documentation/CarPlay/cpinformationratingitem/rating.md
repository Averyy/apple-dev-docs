# rating

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The current rating that the template displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var rating: NSNumber? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSNumber * rating;
```

#### Discussion

This property is an [`NSNumber`](../../Foundation/nsnumber.md) that contains a value in the range of 0 to [`maximumRating`](./maximumrating.md). The value is an increment of 0.5.

## See Also

### Accessing the Item’s Attributes
- [var maximumRating: NSNumber?](./maximumrating.md)
  The maximum rating that the template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationratingitem/rating)*