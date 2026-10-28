# phase

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current press phase of the object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var phase: UIPress.Phase { get }
```

```objc
@property (nonatomic, readonly) UIPressPhase phase;
```

## Discussion

For a list of all possible press phases, see the [`UIPress.Phase`](./phase-swift.enum.md) enumeration.

## See Also

### Getting press attributes
- [var key: UIKey?](./key.md)
  The key pressed or released on a physical keyboard.
- [var type: UIPress.PressType](./type.md)
  The type of the specified press.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when the press occurred or when it was last mutated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/phase-swift.property)*