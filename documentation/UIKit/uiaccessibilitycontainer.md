# UIAccessibilityContainer

**Framework**: UIKit

Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.

## Topics

### Providing information about accessibility elements
- [func accessibilityElementCount() -> Int](../objectivec/nsobject-swift.class/accessibilityelementcount.md)
- [func accessibilityElement(at: Int) -> Any?](../objectivec/nsobject-swift.class/accessibilityelement(at:).md)
- [func index(ofAccessibilityElement: Any) -> Int](../objectivec/nsobject-swift.class/index(ofaccessibilityelement:).md)
- [var accessibilityElements: [Any]?](../objectivec/nsobject-swift.class/accessibilityelements.md)
  An array of features of an object that assistive technologies can access.
- [var automationElements: [Any]?](../objectivec/nsobject-swift.class/automationelements.md)
- [var accessibilityContainerType: UIAccessibilityContainerType](../objectivec/nsobject-swift.class/accessibilitycontainertype.md)
- [enum UIAccessibilityContainerType](uiaccessibilitycontainertype.md)
  Constants that indicate the type of content in a data-based container.
### Useful links
- [Accessibility design for Mac Catalyst](../accessibility/accessibility_design_for_mac_catalyst.md)
  Improve navigation in your app by using keyboard shortcuts and accessibility containers.

## See Also

- [UIAccessibility](uiaccessibility-protocol.md)
  A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md)
  Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainer)*