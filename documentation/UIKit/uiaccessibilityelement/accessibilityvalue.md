# accessibilityValue

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string that represents the current value of the accessibility element.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var accessibilityValue: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * accessibilityValue;
```

#### Discussion

The value is a localized string that contains the current value of an element. For example, the value of a slider might be 9.5 or 35% and the value of a text field is the text it contains.

Use the value property only when an accessibility element can have a value that is not represented by its label. For example, a volume slider’s label might be “Volume,” but its value is the current volume level. In this case, it’s not enough for users to know the identity of the slider, because they also need to know its current value. The label of a Save button, on the other hand, tells users everything they need to know about the control; supplying the word “Save” as a value would be unnecessary and confusing.

## See Also

### Accessing the attributes of an accessibility element
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A string that succinctly identifies the accessibility element.
- [var accessibilityHint: String?](./accessibilityhint.md)
  A string that briefly describes the result of performing an action on the accessibility element.
- [var accessibilityFrame: CGRect](./accessibilityframe.md)
  The frame of the accessibility element, in screen coordinates.
- [var accessibilityFrameInContainerSpace: CGRect](./accessibilityframeincontainerspace.md)
  The frame of the accessibility element, in the coordinate space of its container view.
- [var accessibilityTraits: UIAccessibilityTraits](./accessibilitytraits.md)
  The combination of traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilityvalue)*