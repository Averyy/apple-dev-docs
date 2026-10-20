# UIAccessibilityContainer

**Framework**: UIKit  
**Role**: API Collection

Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.

## Topics

### Providing information about accessibility elements
- [func accessibilityElementCount() -> Int](../ObjectiveC/nsobject-swift.class/accessibilityelementcount%28%29.md)
- [func accessibilityElement(at: Int) -> Any?](../ObjectiveC/nsobject-swift.class/accessibilityelement%28at%29.md)
- [func index(ofAccessibilityElement: Any) -> Int](../ObjectiveC/nsobject-swift.class/index%28ofaccessibilityelement%29.md)
- [var accessibilityElements: [Any]?](../ObjectiveC/nsobject-swift.class/accessibilityelements.md)
  An array of features of an object that assistive technologies can access.
- [var automationElements: [Any]?](../ObjectiveC/nsobject-swift.class/automationelements.md)
- [var accessibilityContainerType: UIAccessibilityContainerType](../ObjectiveC/nsobject-swift.class/accessibilitycontainertype.md)
- [enum UIAccessibilityContainerType](./uiaccessibilitycontainertype.md)
  Constants that indicate the type of content in a data-based container.
### Useful links
- [Accessibility design for Mac Catalyst](../Accessibility/accessibility_design_for_mac_catalyst.md)
  Improve navigation in your app by using keyboard shortcuts and accessibility containers.

## See Also

### Essentials
- [UIAccessibility](./uiaccessibility-protocol.md)
  A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [Supporting VoiceOver in your app](./supporting-voiceover-in-your-app.md)
  Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainer)*