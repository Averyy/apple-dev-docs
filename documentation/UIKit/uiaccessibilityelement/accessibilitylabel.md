# accessibilityLabel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string that succinctly identifies the accessibility element.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var accessibilityLabel: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * accessibilityLabel;
```

## Mentions

- [Supporting VoiceOver in your app](../supporting-voiceover-in-your-app.md)

## Discussion

The label is a very short, localized string that identifies the accessibility element, but does not include the type of the control or view. For example, the label for a Save button is “Save,” not “Save button.”

By default, standard UIKit controls and views have labels that derive from their titles. If you provide a custom control or view, however, you need to set this property appropriately so that assistive applications can supply accurate information to users with disabilities.

## See Also

### Accessing the attributes of an accessibility element
- [var accessibilityHint: String?](./accessibilityhint.md)
  A string that briefly describes the result of performing an action on the accessibility element.
- [var accessibilityValue: String?](./accessibilityvalue.md)
  A string that represents the current value of the accessibility element.
- [var accessibilityFrame: CGRect](./accessibilityframe.md)
  The frame of the accessibility element, in screen coordinates.
- [var accessibilityFrameInContainerSpace: CGRect](./accessibilityframeincontainerspace.md)
  The frame of the accessibility element, in the coordinate space of its container view.
- [var accessibilityTraits: UIAccessibilityTraits](./accessibilitytraits.md)
  The combination of traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilitylabel)*