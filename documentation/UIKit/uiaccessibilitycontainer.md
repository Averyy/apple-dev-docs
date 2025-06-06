# UIAccessibilityContainer

**Framework**: UIKit

Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.

## Topics

### Providing information about accessibility elements
- [@MainActor func accessibilityElementCount() -> Int](../ObjectiveC/NSObject-swift.class/accessibilityElementCount.md)
- [@MainActor func accessibilityElement(at index: Int) -> Any?](../ObjectiveC/NSObject-swift.class/accessibilityElement(at:).md)
- [@MainActor func index(ofAccessibilityElement element: Any) -> Int](../ObjectiveC/NSObject-swift.class/index(ofAccessibilityElement:).md)
- [@MainActor var accessibilityElements: [Any]? { get set }](../ObjectiveC/NSObject-swift.class/accessibilityElements.md)
- [@MainActor var automationElements: [Any]? { get set }](../ObjectiveC/NSObject-swift.class/automationElements.md)
- [@MainActor var accessibilityContainerType: UIAccessibilityContainerType { get set }](../ObjectiveC/NSObject-swift.class/accessibilityContainerType.md)
- [enum UIAccessibilityContainerType](uiaccessibilitycontainertype.md)
  Constants that indicate the type of content in a data-based container.
### Useful links
- [Accessibility design for Mac Catalyst](../Accessibility/accessibility_design_for_mac_catalyst.md)
  Improve navigation in your app by using keyboard shortcuts and accessibility containers.

## See Also

- [UIAccessibility](uiaccessibility-protocol.md)
  A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md)
  Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainer)*