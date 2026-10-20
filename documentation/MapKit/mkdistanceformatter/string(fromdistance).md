# string(fromDistance:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Creates a string representation of the specified distance.

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
func string(fromDistance distance: CLLocationDistance) -> String
```

```objc
- (NSString *) stringFromDistance:(CLLocationDistance) distance;
```

#### Return Value

A user-readable string that describes the distance based on the formatter settings.

## Parameters

- `distance`: The distance value that you want to convert to a string.

## See Also

### Converting distances
- [func distance(from: String) -> CLLocationDistance](./distance%28from%29.md)
  Returns the distance value parsed from the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/string(fromdistance:))*