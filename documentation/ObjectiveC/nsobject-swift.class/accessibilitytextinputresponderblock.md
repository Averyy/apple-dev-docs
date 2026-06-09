# accessibilityTextInputResponderBlock

**Framework**: Objective-C Runtime  
**Kind**: property

The block to use to handle text input calls to a backing view.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- visionOS 2.1+

## Declaration

```swift
@MainActor
var accessibilityTextInputResponderBlock: AXUITextInputReturnBlock? { get set }
```

#### Discussion

If your accessibility element represents a view that supports text operations using the [`UITextInput`](https://developer.apple.com/documentation/UIKit/UITextInput) protocol, use this property to forward `UITextInput` calls to your backing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponderblock)*