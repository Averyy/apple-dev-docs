# Integrating accessibility into your app

**Framework**: Accessibility

Make your app more accessible to users with disabilities by adding accessibility features.

**Availability**:
- macOS 13.1+
- Xcode 14.2+

#### Overview

By adding accessibility features to your app, you make it available to a wider range of users. This sample code project shows how to implement accessibility for several common UI controls. The examples make the controls accessible by using accessibility properties, accessibility protocols, and the [`NSAccessibilityElement`](https://developer.apple.com/documentation/AppKit/NSAccessibilityElement-swift.class) class.

In macOS 10.10, the Accessibility API moved to a protocol-based approach, in contrast to the key-based API from macOS 10.9 and earlier. With the protocol-based API, you can:

- Simplify the implementation of accessibility
- More closely align macOS accessibility features with those of iOS
- Ensure compatibility with existing macOS apps and code

Accessibility API features in macOS versions earlier than 10.10 are deprecated, but can coexist with the current API. No changes are required for apps or accessibility clients that use earlier versions of the Accessibility API. If you implement both APIs on the same class, the current API takes precedence for that class. For cell-based controls, you need to provide Accessibility API implementations on the cell.

##### Add Accessibility Attributes

Most accessibility attributes from macOS 10.9 and earlier are now properties in the following AppKit classes:

- `NSApplication`
- `NSWindow`
- `NSView`
- `NSDrawer`
- `NSPopover`
- `NSCell`

To set an accessibility attribute value on an instance of one of these classes (or a subclass), simply assign the value to the property.

```swift
button.setAccessibilityLabel(NSLocalizedString("My label", comment: "label to use for this button"))
```

[`View in Source`](https://developer.apple.comx-source-tag://setAccessibilityLabel)

Alternatively, you can override the getter in the subclass’s implementation.

```swift
override func accessibilityLabel() -> String? {
    return NSLocalizedString("Play", comment: "accessibility label of the Play button")
}
```

[`View in Source`](https://developer.apple.comx-source-tag://accessibilityLabel)

[`NSAccessibility`](https://developer.apple.com/documentation/AppKit/nsaccessibility) contains the full list of accessibility properties.

##### Add Accessibility Protocols to Custom Controls

The Accessibility API protocols define the required accessibility functions for many common accessibility elements. Conformance to an accessibility protocol isn’t required to use the API, but it’s recommended when making custom controls accessible. Conforming to an accessibility protocol results in a warning for each unimplemented required function and allows the system to automatically infer the  [`accessibilityRole`](https://developer.apple.com/documentation/AppKit/NSAccessibility-c.protocol/accessibilityRole) and [`isAccessibilityElement()`](https://developer.apple.com/documentation/AppKit/NSAccessibilityProtocol/isAccessibilityElement()) properties.

Standard AppKit controls conform to the related accessibility protocol (for example, [`NSButton`](https://developer.apple.com/documentation/AppKit/NSButton) conforms to the [`NSAccessibilityButton`](https://developer.apple.com/documentation/AppKit/NSAccessibilityButton) protocol, and [`NSSlider`](https://developer.apple.com/documentation/AppKit/NSSlider) conforms to the [`NSAccessibilitySlider`](https://developer.apple.com/documentation/AppKit/NSAccessibilitySlider) protocol). Whenever possible, subclass from the appropriate AppKit control to leverage the built-in accessibility.

To add accessibility to a custom control:

1. Conform to the appropriate protocol.
2. Implement all the required functions. A warning appears for each unimplemented required function.
3. Test using VoiceOver and the Accessibility Inspector.

For example, the following code sample creates a custom control that subclasses `NSView` and draws and behaves like a button:

```swift
class CustomButtonView: NSView {
```

[`View in Source`](https://developer.apple.comx-source-tag://customButtonDeclare)

If a custom control doesn’t conform to an accessibility protocol, you need to implement the [`accessibilityRole`](https://developer.apple.com/documentation/AppKit/NSAccessibility-c.protocol/accessibilityRole) and [`isAccessibilityElement()`](https://developer.apple.com/documentation/AppKit/NSAccessibilityProtocol/isAccessibilityElement()) functions.

```swift
override func accessibilityRole() -> NSAccessibility.Role? {
    return NSAccessibility.Role.button
}

override func isAccessibilityElement() -> Bool {
    return true
}
```

[`View in Source`](https://developer.apple.comx-source-tag://customButtonAdoption)

##### Create an Accessibility Element

For objects that don’t have a backing view — for example, a single view that draws several images, each of which is individually accessible — create an instance of `NSAccessibilityElement` for each object, and return an array of the instances from the containing view’s `accessibilityChildren` function.

##### Simplify Your Accessibility Code

`NSAccessibilityElement` has two convenience methods that simplify its use:

- [`accessibilityAddChildElement(_:)`](https://developer.apple.com/documentation/AppKit/NSAccessibilityElement-swift.class/accessibilityAddChildElement(_:)) — This function sets the specified element as a subelement of the receiver’s [`accessibilityChildren`](https://developer.apple.com/documentation/AppKit/NSAccessibility-c.protocol/accessibilityChildren) and the receiver as the container to the specified element. This behavior is useful when you create hierarchies of accessibility elements.
- [`accessibilityFrameInParentSpace()`](https://developer.apple.com/documentation/AppKit/NSAccessibilityElement-swift.class/accessibilityFrameInParentSpace()) — This property allows the accessibility element to specify its frame relative to its accessibility container, so that the system can automatically recalculate the  [`accessibilityFrame()`](https://developer.apple.com/documentation/AppKit/NSAccessibilityElementProtocol/accessibilityFrame()) property value (given in screen coordinates) whenever the element or any of its containing views changes location.

The Accessibility API includes two convenience methods in `AppKit/NSAccessibility.h` to simplify common accessibility tasks:

- [`screenRect(fromView:rect:)`](https://developer.apple.com/documentation/AppKit/NSAccessibility-swift.struct/screenRect(fromView:rect:)) — This convenience method converts `frame` from the `parentView` coordinate space to the screen coordinate space. This is useful when you set an object’s accessibility frame using the [`accessibilityFrame()`](https://developer.apple.com/documentation/AppKit/NSAccessibilityProtocol/accessibilityFrame()) method.
- [`screenPoint(fromView:point:)`](https://developer.apple.com/documentation/AppKit/NSAccessibility-swift.struct/screenPoint(fromView:point:)) — This convenience method converts `point` from the `parentView` coordinate space to the screen coordinate space. This is useful when you calculate an object’s [`accessibilityActivationPoint()`](https://developer.apple.com/documentation/AppKit/NSAccessibilityProtocol/accessibilityActivationPoint()) coordinates.

##### Test the Accessibility Features on Your App

The Accessibility Inspector is an Xcode tool that displays all accessibility information for the element currently beneath the cursor, including the accessibility hierarchy, accessibility attributes, and accessibility actions. It also shows warnings for common accessibility problems, such as a missing accessibility label. Launch the Accessibility Inspector from the Xcode > Open Developer Tool menu.

To test VoiceOver, choose System Settings > Accessibility > VoiceOver and click the toggle to enable it, or press Command-F5. To learn how to use VoiceOver, choose System Settings > Accessibility > VoiceOver > Open VoiceOver Training.

## See Also

- [Enhancing the accessibility of your SwiftUI app](enhancing-the-accessibility-of-your-swiftui-app.md)
  Support advancements in SwiftUI accessibility to make your app accessible to everyone.
- [Creating Accessible Views](../swiftui/creating_accessible_views.md)
  Make your app accessible to everyone by applying accessibility modifiers to your SwiftUI views.
- [Delivering an exceptional accessibility experience](delivering_an_exceptional_accessibility_experience.md)
  Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.
- [Accessibility design for Mac Catalyst](accessibility_design_for_mac_catalyst.md)
  Improve navigation in your app by using keyboard shortcuts and accessibility containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/integrating_accessibility_into_your_app)*