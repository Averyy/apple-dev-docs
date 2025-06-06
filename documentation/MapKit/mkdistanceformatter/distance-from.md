# distance(from:)

**Framework**: MapKit  
**Kind**: method

Returns the distance value parsed from the specified string.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func distance(from distance: String) -> CLLocationDistance
```

#### Return Value

The distance value represented by the string or `-1.0` if the string does not contain a recognized distance value.

#### Discussion

This method searches the provided string for a number that could represent a distance. Specify distances as purely numerical values. Don’t specify distances as fractions such as “1/4 mile,” use distances and standard distance designations instead, such as “0.25 miles,” “1.2 km,” “120 yards,” and so on.

## Parameters

- `distance`: A formatted string that specifies a distance.

## See Also

- [func string(fromDistance: CLLocationDistance) -> String](mkdistanceformatter/string(fromdistance:).md)
  Creates a string representation of the specified distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/distance(from:))*