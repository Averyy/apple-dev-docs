# bounds

**Framework**: RealityKit  
**Kind**: property

The bounding box to encompass all of the instances this group part draws.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var bounds: BoundingBox?
```

#### Discussion

If bounds is `nil`, RealityKit calculates a bounding box for you each time you update your instances within [`LowLevelInstanceData`](lowlevelinstancedata.md).

Automatic bounds calculation is not supported when [`LowLevelInstanceData`](lowlevelinstancedata.md) is updated via [`replace(using:)`](lowlevelinstancedata/replace(using:).md). Provide a non-nil bounds value when updating instances with Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancescomponent/part/bounds)*