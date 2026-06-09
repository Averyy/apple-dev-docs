# accessibilityTextInputResponder

**Framework**: Objective-C Runtime  
**Kind**: property

The object that handles text input calls for this accessibility element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- visionOS 2.1+

## Declaration

```swift
@MainActor
weak var accessibilityTextInputResponder: (any UITextInput)? { get set }
```

#### Discussion

If your accessibility element represents a view that supports text operations using the [`UITextInput`](https://developer.apple.com/documentation/UIKit/UITextInput) protocol, use this property to forward `UITextInput` calls to your backing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponder)*