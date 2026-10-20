# accessibilityElementDidLoseFocus()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent after an assistive technology has removed its virtual focus from an accessibility element.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityElementDidLoseFocus()
```

```objc
- (void) accessibilityElementDidLoseFocus;
```

#### Discussion

Override `accessibilityElementDidLoseFocus` if you need to know when an assistive technology has removed its virtual focus from an accessibility element. Note that `accessibilityElementDidLoseFocus` is sent before [`accessibilityElementDidBecomeFocused()`](./accessibilityelementdidbecomefocused%28%29.md).

## See Also

### Getting focus information
- [func accessibilityElementDidBecomeFocused()](./accessibilityelementdidbecomefocused%28%29.md)
  Sent after an assistive technology has set its virtual focus on the accessibility element.
- [func accessibilityElementIsFocused() -> Bool](./accessibilityelementisfocused%28%29.md)
  Returns a Boolean value indicating whether an assistive technology is focused on the accessibility element.
- [func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<UIAccessibility.AssistiveTechnologyIdentifier>?](./accessibilityassistivetechnologyfocusedidentifiers%28%29.md)
  Returns a set of identifier keys indicating which assistive app has focus on the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelementdidlosefocus())*