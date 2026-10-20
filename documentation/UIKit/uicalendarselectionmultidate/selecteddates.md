# selectedDates

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of date component objects that represent selected dates in a calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var selectedDates: [DateComponents] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSDateComponents *> * selectedDates;
```

## See Also

### Updating the selected dates
- [func setSelectedDates([DateComponents], animated: Bool)](./setselecteddates%28_,animated%29.md)
  Updates the array of date component objects that represent selected dates in a calendar view, with an option to animate the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidate/selecteddates)*