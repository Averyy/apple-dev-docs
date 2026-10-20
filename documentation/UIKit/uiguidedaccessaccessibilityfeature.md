# UIGuidedAccessAccessibilityFeature

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UIGuidedAccessAccessibilityFeature : NSUInteger;
```

## Topics

### Constants
- [static var assistiveTouch: UIGuidedAccessAccessibilityFeature](./uiguidedaccessaccessibilityfeature/assistivetouch.md)
  The AssistiveTouch accessibility feature.
- [static var grayscaleDisplay: UIGuidedAccessAccessibilityFeature](./uiguidedaccessaccessibilityfeature/grayscaledisplay.md)
  The Grayscale accessibility feature.
- [static var invertColors: UIGuidedAccessAccessibilityFeature](./uiguidedaccessaccessibilityfeature/invertcolors.md)
  The Smart Invert accessibility feature.
- [static var voiceOver: UIGuidedAccessAccessibilityFeature](./uiguidedaccessaccessibilityfeature/voiceover.md)
  The VoiceOver assistive app.
- [static var zoom: UIGuidedAccessAccessibilityFeature](./uiguidedaccessaccessibilityfeature/zoom.md)
  The Zoom accessibility feature.
### Initializers
- [init(rawValue: UInt)](./uiguidedaccessaccessibilityfeature/init%28rawvalue%29.md)
  Creates a Guided Access accessibility feature with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Guided Access
- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](./uiaccessibility/configureforguidedaccess%28features,enabled,completionhandler%29.md)
  Enables or disables the specified accessibility features while using Guided Access.
- [UIAccessibility.GuidedAccessError.Code](./uiaccessibility/guidedaccesserror/code.md)
  Error codes for Guided Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiguidedaccessaccessibilityfeature)*