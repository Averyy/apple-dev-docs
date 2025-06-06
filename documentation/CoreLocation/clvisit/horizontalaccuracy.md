# horizontalAccuracy

**Framework**: Core Location  
**Kind**: property

The horizontal accuracy (in meters) of the specified coordinate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var horizontalAccuracy: CLLocationAccuracy { get }
```

#### Discussion

The latitude and longitude specified by the [`coordinate`](clvisit/coordinate.md) property identify the center of the circle, and this value indicates the radius of that circle.

## See Also

- [var coordinate: CLLocationCoordinate2D](clvisit/coordinate.md)
  The geographical coordinate information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clvisit/horizontalaccuracy)*