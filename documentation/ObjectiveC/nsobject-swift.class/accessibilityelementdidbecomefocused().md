# accessibilityElementDidBecomeFocused()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent after an assistive technology has set its virtual focus on the accessibility element.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityElementDidBecomeFocused()
```

```objc
- (void) accessibilityElementDidBecomeFocused;
```

#### Discussion

Override `accessibilityElementDidBecomeFocused` if you need to know when an assistive technology has set its virtual focus on an accessibility element.

## See Also

### Getting focus information
- [func accessibilityElementDidLoseFocus()](./accessibilityelementdidlosefocus%28%29.md)
  Sent after an assistive technology has removed its virtual focus from an accessibility element.
- [func accessibilityElementIsFocused() -> Bool](./accessibilityelementisfocused%28%29.md)
  Returns a Boolean value indicating whether an assistive technology is focused on the accessibility element.
- [func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<UIAccessibility.AssistiveTechnologyIdentifier>?](./accessibilityassistivetechnologyfocusedidentifiers%28%29.md)
  Returns a set of identifier keys indicating which assistive app has focus on the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelementdidbecomefocused())*