# UIGuidedAccessAccessibilityFeature

**Framework**: UIKit  
**Kind**: struct

Constants that describe accessibility features for Guided Access.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct UIGuidedAccessAccessibilityFeature
```

## Topics

### Constants
- [static var assistiveTouch: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/assistivetouch.md)
  The AssistiveTouch accessibility feature.
- [static var grayscaleDisplay: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/grayscaledisplay.md)
  The Grayscale accessibility feature.
- [static var invertColors: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/invertcolors.md)
  The Smart Invert accessibility feature.
- [static var voiceOver: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/voiceover.md)
  The VoiceOver assistive app.
- [static var zoom: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/zoom.md)
  The Zoom accessibility feature.
### Initializers
- [init(rawValue: UInt)](uiguidedaccessaccessibilityfeature/init(rawvalue:).md)
  Creates a Guided Access accessibility feature with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:).md)
  Enables or disables the specified accessibility features while using Guided Access.
- [UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/code.md)
  Error codes for Guided Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiguidedaccessaccessibilityfeature)*