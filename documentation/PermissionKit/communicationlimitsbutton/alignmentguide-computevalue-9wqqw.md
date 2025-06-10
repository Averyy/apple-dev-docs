# alignmentGuide(_:computeValue:)

**Framework**: PermissionKit  
**Kind**: method

Returns a view modified so that its value for the given `guide` is the result of passing the `ViewDimensions` of the underlying element to `computeValue`.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func alignmentGuide(_ g: DepthAlignment, computeValue: @escaping (ViewDimensions3D) -> CGFloat) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/alignmentguide(_:computevalue:)-9wqqw)*