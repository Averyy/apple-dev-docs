# UIAccessibilityCustomRotorItemResult

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIAccessibilityCustomRotorItemResult : NSObject
```

## Topics

### Creating a rotor item result
- [init(targetElement: any NSObjectProtocol, targetRange: UITextRange?)](./uiaccessibilitycustomrotoritemresult/init%28targetelement,targetrange%29.md)
  Creates a rotor item result from the specified target element and text range.
### Getting information about the target element
- [var targetElement: (any NSObjectProtocol)?](./uiaccessibilitycustomrotoritemresult/targetelement.md)
  The target element of the rotor.
- [var targetRange: UITextRange?](./uiaccessibilitycustomrotoritemresult/targetrange.md)
  The text range (if any) of the target element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Navigation
- [class UIAccessibilityCustomRotor](./uiaccessibilitycustomrotor.md)
  A context-sensitive function that helps VoiceOver users find the next instance of a related element.
- [class UIAccessibilityCustomRotorSearchPredicate](./uiaccessibilitycustomrotorsearchpredicate.md)
  The search parameters that help determine the next matching custom rotor item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult)*