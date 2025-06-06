# UIAccessibilityElement

**Framework**: UIKit  
**Kind**: class

An element that should be accessible to users with disabilities, but that isn’t accessible by default.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAccessibilityElement
```

## Mentions

- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md)

#### Overview

You can use [`UIAccessibilityElement`](uiaccessibilityelement.md) to provide information about an icon or text image that isn’t automatically accessible because it doesn’t inherit from [`UIView`](uiview.md) (or [`UIControl`](uicontrol.md)). A view that contains such nonview items creates an instance of [`UIAccessibilityElement`](uiaccessibilityelement.md) to represent each item that needs to be accessible.

The properties of an accessibility element provide information about the element, such as location and current value, to an assistive application. You might need to set an element’s property even if you don’t need to create an instance of `UIAccessibilityElement` to represent it. For example, if your app includes a button with a custom icon that means “solve,” the button itself is already represented by an accessibility element because it’s a subclass of [`UIButton`](uibutton.md). However, you need to supply information for the label and hint properties because this information is unique to this button. You can do this in Interface Builder or by setting the properties in the [`UIAccessibility`](uiaccessibility-protocol.md) informal protocol.

## Topics

### Creating an accessibility element
- [init(accessibilityContainer: Any)](uiaccessibilityelement/init(accessibilitycontainer:).md)
  Creates and initializes an accessibility element to represent an item in the specified container.
### Accessing the containing view
- [var accessibilityContainer: AnyObject?](uiaccessibilityelement/accessibilitycontainer.md)
  The view that contains the accessibility element.
### Determining accessibility
- [var isAccessibilityElement: Bool](uiaccessibilityelement/isaccessibilityelement.md)
  A Boolean value indicating whether the item is an accessibility element an assistive application can access.
### Accessing the attributes of an accessibility element
- [var accessibilityLabel: String?](uiaccessibilityelement/accessibilitylabel.md)
  A string that succinctly identifies the accessibility element.
- [var accessibilityHint: String?](uiaccessibilityelement/accessibilityhint.md)
  A string that briefly describes the result of performing an action on the accessibility element.
- [var accessibilityValue: String?](uiaccessibilityelement/accessibilityvalue.md)
  A string that represents the current value of the accessibility element.
- [var accessibilityFrame: CGRect](uiaccessibilityelement/accessibilityframe.md)
  The frame of the accessibility element, in screen coordinates.
- [var accessibilityFrameInContainerSpace: CGRect](uiaccessibilityelement/accessibilityframeincontainerspace.md)
  The frame of the accessibility element, in the coordinate space of its container view.
- [var accessibilityTraits: UIAccessibilityTraits](uiaccessibilityelement/accessibilitytraits.md)
  The combination of traits that best characterize the accessibility element.

## Relationships

### Inherits From
- [UIResponder](uiresponder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [protocol UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md)
  A set of methods you can implement to provide accessibility information for a scroll view.
- [protocol UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md)
  A set of methods you can implement to provide accessibility information for individual components of a picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement)*