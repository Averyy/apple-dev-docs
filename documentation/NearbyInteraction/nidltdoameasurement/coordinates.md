# coordinates

**Framework**: Nearby Interaction  
**Kind**: property

Indicates the anchor’s coordinates:

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var coordinates: simd_double3 { get }
```

#### Discussion

When coordinatesType == NIDLTDOACoordinatesTypeGeodetic: coordinates represent geodetic position in 3D space with format {latitude, longitude, altitude}. When coordinatesType == NIDLTDOACoordinatesTypeRelative: coordinates represent distances from anchor(s) along the 3 axes in 3D space  with format {x, y, z}.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/coordinates)*