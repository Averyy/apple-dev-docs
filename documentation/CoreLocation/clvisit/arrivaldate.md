# arrivalDate

**Framework**: Core Location  
**Kind**: property

The approximate time at which the user arrived at the specified location.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var arrivalDate: Date { get }
```

#### Discussion

When the visit object does not include arrival information, this property is set to the date returned by the [`distantPast`](https://developer.apple.com/documentation/foundation/nsdate/1418197-distantpast) method of [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate).

## See Also

- [var departureDate: Date](clvisit/departuredate.md)
  The approximate time at which the user left the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clvisit/arrivaldate)*