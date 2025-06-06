# verticalAccuracy

**Framework**: Core Location  
**Kind**: property

The validity of the altitude values, and their estimated uncertainty, measured in meters.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var verticalAccuracy: CLLocationAccuracy { get }
```

#### Discussion

A positive [`verticalAccuracy`](cllocation/verticalaccuracy.md) value represents the estimated uncertainty associated with [`altitude`](cllocation/altitude.md) and [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md). This value is available whenever altitude values are available.

If [`verticalAccuracy`](cllocation/verticalaccuracy.md) is `0` or a negative number, [`altitude`](cllocation/altitude.md) and [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) values are invalid. If [`verticalAccuracy`](cllocation/verticalaccuracy.md) is a postive number, [`altitude`](cllocation/altitude.md) and [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) values are valid.

A positive [`verticalAccuracy`](cllocation/verticalaccuracy.md) value represents an uncertainty that’s approximately 68 percent, or one standard deviation, above and below the altitude values.

> **Note**:  In iOS, this property is declared as `nonatomic`. In macOS, it’s declared as `atomic`.

 In iOS, this property is declared as `nonatomic`. In macOS, it’s declared as `atomic`.

## See Also

- [var horizontalAccuracy: CLLocationAccuracy](cllocation/horizontalaccuracy.md)
  The radius of uncertainty for the location, measured in meters.
- [typealias CLLocationAccuracy](cllocationaccuracy.md)
  The accuracy of a geographical coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/verticalaccuracy)*