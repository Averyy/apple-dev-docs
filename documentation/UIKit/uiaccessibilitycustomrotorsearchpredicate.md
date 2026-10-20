# UIAccessibilityCustomRotorSearchPredicate

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The search parameters that help determine the next matching custom rotor item result.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAccessibilityCustomRotorSearchPredicate
```

```objc
@interface UIAccessibilityCustomRotorSearchPredicate : NSObject
```

## Topics

### Configuring search parameters
- [var currentItem: UIAccessibilityCustomRotorItemResult](./uiaccessibilitycustomrotorsearchpredicate/currentitem.md)
  The current element of the search.
- [var searchDirection: UIAccessibilityCustomRotor.Direction](./uiaccessibilitycustomrotorsearchpredicate/searchdirection.md)
  The direction in which to search.
- [UIAccessibilityCustomRotor.Direction](./uiaccessibilitycustomrotor/direction.md)
  Constants that indicate the search direction.

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
- [class UIAccessibilityCustomRotorItemResult](./uiaccessibilitycustomrotoritemresult.md)
  A target element that a custom rotor references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotorsearchpredicate)*