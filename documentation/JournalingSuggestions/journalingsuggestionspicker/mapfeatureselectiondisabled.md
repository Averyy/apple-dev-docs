# mapFeatureSelectionDisabled(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Specifies which map features should have selection disabled.

**Availability**:
- iOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapFeatureSelectionDisabled(_ selectionDisabled: @escaping (MapFeature) -> Bool) -> some View
```

#### Discussion

The `selectionDisabled` parameter takes a closure which maps map features, to booleans. If that closure returns true for a given map feature, that map feature will be considered unselectable.

## Parameters

- `selectionDisabled`: Determines if selection should be disabled for a given   map feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapfeatureselectiondisabled(_:))*