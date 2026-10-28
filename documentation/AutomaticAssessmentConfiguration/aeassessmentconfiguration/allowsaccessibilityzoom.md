# allowsAccessibilityZoom

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow Zoom during an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var allowsAccessibilityZoom: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsAccessibilityZoom;
```

## Discussion

Users can enable Zoom in the Settings app (Accessibility > Zoom) to magnify the screen. An assessment session **does not** disable Zoom by default, but you can disable it by setting [`allowsAccessibilityZoom`](./allowsaccessibilityzoom.md) to `NO` in the [`AEAssessmentConfiguration`](../aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityzoom)*