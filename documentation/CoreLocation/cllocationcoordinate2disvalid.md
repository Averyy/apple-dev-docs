# CLLocationCoordinate2DIsValid(_:)

**Framework**: Core Location  
**Kind**: func

Returns a Boolean value indicating whether the specified coordinate is valid.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CLLocationCoordinate2DIsValid(_ coord: CLLocationCoordinate2D) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the coordinate is valid or [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

#### Discussion

A coordinate is considered invalid if it meets at least one of the following criteria:

- Its latitude is greater than 90 degrees or less than -90 degrees.
- Its longitude is greater than 180 degrees or less than -180 degrees.

## Parameters

- `coord`: A coordinate containing latitude and longitude values.

## See Also

- [let kCLLocationCoordinate2DInvalid: CLLocationCoordinate2D](kcllocationcoordinate2dinvalid.md)
  An invalid coordinate value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2disvalid(_:))*