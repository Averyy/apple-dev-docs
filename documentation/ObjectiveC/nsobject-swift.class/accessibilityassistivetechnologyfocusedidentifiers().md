# accessibilityAssistiveTechnologyFocusedIdentifiers()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a set of identifier keys indicating which assistive app has focus on the accessibility element.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<UIAccessibility.AssistiveTechnologyIdentifier>?
```

```objc
- (NSSet<NSString *> *) accessibilityAssistiveTechnologyFocusedIdentifiers;
```

## See Also

### Getting focus information
- [func accessibilityElementDidBecomeFocused()](./accessibilityelementdidbecomefocused%28%29.md)
  Sent after an assistive technology has set its virtual focus on the accessibility element.
- [func accessibilityElementDidLoseFocus()](./accessibilityelementdidlosefocus%28%29.md)
  Sent after an assistive technology has removed its virtual focus from an accessibility element.
- [func accessibilityElementIsFocused() -> Bool](./accessibilityelementisfocused%28%29.md)
  Returns a Boolean value indicating whether an assistive technology is focused on the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers())*