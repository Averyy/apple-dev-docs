# key

**Framework**: UIKit  
**Kind**: property

The key pressed or released on a physical keyboard.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var key: UIKey? { get }
```

## Mentions

- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md)

#### Discussion

This property is `nil` when the press event isn’t from a keyboard; for example, a button press on an Apple TV remote.

## See Also

- [var type: UIPress.PressType](uipress/type.md)
  The type of the specified press.
- [var phase: UIPress.Phase](uipress/phase-swift.property.md)
  The current press phase of the object.
- [var timestamp: TimeInterval](uipress/timestamp.md)
  The time when the press occurred or when it was last mutated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/key)*