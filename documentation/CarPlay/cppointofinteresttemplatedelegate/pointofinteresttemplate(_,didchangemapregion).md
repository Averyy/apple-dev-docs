# pointOfInterestTemplate(_:didChangeMapRegion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate about changes to the visible region of the template’s map.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func pointOfInterestTemplate(_ pointOfInterestTemplate: CPPointOfInterestTemplate, didChangeMapRegion region: MKCoordinateRegion)
```

```objc
- (void) pointOfInterestTemplate:(CPPointOfInterestTemplate *) pointOfInterestTemplate didChangeMapRegion:(MKCoordinateRegion) region;
```

## Discussion

CarPlay calls this method whenever the user pans the template’s map and its visible region changes. In response, re-evaluate which points of interest are relevant to the new region and, if necessary, call [`setPointsOfInterest(_:selectedIndex:)`](../cppointofinteresttemplate/setpointsofinterest%28_,selectedindex%29.md) to update the template.

## Parameters

- `region`: The map’s new visible region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplatedelegate/pointofinteresttemplate(_:didchangemapregion:))*