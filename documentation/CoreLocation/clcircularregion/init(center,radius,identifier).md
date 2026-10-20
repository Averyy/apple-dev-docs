# init(center:radius:identifier:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Creates and returns a region object defining a circular geographic area.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)
```

```objc
- (instancetype) initWithCenter:(CLLocationCoordinate2D) center radius:(CLLocationDistance) radius identifier:(NSString *) identifier;
```

#### Return Value

An initialized region object.

#### Discussion

When defining a geographic region, remember that the location manager doesn’t generate notifications immediately upon crossing a region boundary. Instead, it applies time and distance criteria to ensure that the crossing is intentional and needs to trigger a notification. So choose a center point and radius that are appropriate and give you enough time to alert the user. For more information, see the information about region monitoring in [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497).

## Parameters

- `center`: The center point of the geographic region to monitor.
- `radius`: The distance (measured in meters) from the center point of the geographic region to the edge of the circular boundary.
- `identifier`: A unique identifier to associate with the region object. You use this identifier to differentiate regions within your app. This value can’t be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcircularregion/init(center:radius:identifier:))*