# UIAccessibilityCustomRotorItemResult

**Framework**: UIKit  
**Kind**: class

A target element that a custom rotor references.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAccessibilityCustomRotorItemResult
```

## Topics

### Creating a rotor item result
- [init(targetElement: any NSObjectProtocol, targetRange: UITextRange?)](uiaccessibilitycustomrotoritemresult/init(targetelement:targetrange:).md)
  Creates a rotor item result from the specified target element and text range.
### Getting information about the target element
- [var targetElement: (any NSObjectProtocol)?](uiaccessibilitycustomrotoritemresult/targetelement.md)
  The target element of the rotor.
- [var targetRange: UITextRange?](uiaccessibilitycustomrotoritemresult/targetrange.md)
  The text range (if any) of the target element.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class UIAccessibilityCustomRotor](uiaccessibilitycustomrotor.md)
  A context-sensitive function that helps VoiceOver users find the next instance of a related element.
- [class UIAccessibilityCustomRotorSearchPredicate](uiaccessibilitycustomrotorsearchpredicate.md)
  The search parameters that help determine the next matching custom rotor item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult)*