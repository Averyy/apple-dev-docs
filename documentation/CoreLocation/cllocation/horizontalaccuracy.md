# horizontalAccuracy

**Framework**: Core Location  
**Kind**: property

The radius of uncertainty for the location, measured in meters.

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
var horizontalAccuracy: CLLocationAccuracy { get }
```

#### Discussion

The location’s latitude and longitude identify the center of the circle, and this value indicates the radius of that circle. A negative value indicates that the latitude and longitude are invalid.

##### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

- [var verticalAccuracy: CLLocationAccuracy](cllocation/verticalaccuracy.md)
  The validity of the altitude values, and their estimated uncertainty, measured in meters.
- [typealias CLLocationAccuracy](cllocationaccuracy.md)
  The accuracy of a geographical coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/horizontalaccuracy)*