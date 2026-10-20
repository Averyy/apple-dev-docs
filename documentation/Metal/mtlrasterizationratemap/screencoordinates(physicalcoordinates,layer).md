# screenCoordinates(physicalCoordinates:layer:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Converts a point in physical coordinates inside a layer to its corresponding logical viewport coordinates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func screenCoordinates(physicalCoordinates: MTLCoordinate2D, layer layerIndex: Int) -> MTLCoordinate2D
```

```objc
- (MTLCoordinate2D) mapPhysicalToScreenCoordinates:(MTLCoordinate2D) physicalCoordinates forLayer:(NSUInteger) layerIndex;
```

#### Return Value

A point in the view coordinates corresponding to the source point.

#### Discussion

The returned coordinates are always greater than or equal to the input coordinates because the rasterization rate never exceeds 1:1 in any region.

## Parameters

- `physicalCoordinates`: A point in layer coordinates.
- `layerIndex`: The index of the rate map to use.

## See Also

### Converting between viewport and physical coordinates
- [func physicalCoordinates(screenCoordinates: MTLCoordinate2D, layer: Int) -> MTLCoordinate2D](./physicalcoordinates%28screencoordinates,layer%29.md)
  Converts a point in logical viewport coordinates to the corresponding physical coordinates in a render layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/screencoordinates(physicalcoordinates:layer:))*