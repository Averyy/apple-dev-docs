# departureDate

**Framework**: Core Location  
**Kind**: property

The approximate time at which the user left the specified location.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var departureDate: Date { get }
```

#### Discussion

When the visit object does not include departure information, this property is set to the date returned by the [`distantFuture`](https://developer.apple.com/documentation/Foundation/NSDate/distantFuture) method of [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate).

## See Also

- [var arrivalDate: Date](clvisit/arrivaldate.md)
  The approximate time at which the user arrived at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clvisit/departuredate)*