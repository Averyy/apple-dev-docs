# maximumRating

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The maximum rating that the template displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var maximumRating: NSNumber? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSNumber * maximumRating;
```

## Discussion

This property is an [`NSNumber`](../../Foundation/nsnumber.md) that contains a value in the range of 1 to 5. The value is a whole number.

## See Also

### Accessing the Item’s Attributes
- [var rating: NSNumber?](./rating.md)
  The current rating that the template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationratingitem/maximumrating)*