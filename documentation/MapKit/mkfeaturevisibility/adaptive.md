# MKFeatureVisibility.adaptive

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

A constant indicating that the feature adapts to the current map state.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case adaptive
```

```c
MKFeatureVisibilityAdaptive
```

#### Discussion

The framework displays title text and hides subtitle text for features in the normal state. When selected, the framework hides the feature’s title and subtitle text when the feature requires a callout.

## See Also

### Visibility options
- [MKFeatureVisibility.hidden](./hidden.md)
  A constant indicating that the feature is hidden.
- [MKFeatureVisibility.visible](./visible.md)
  A constant indicating that the feature is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkfeaturevisibility/adaptive)*