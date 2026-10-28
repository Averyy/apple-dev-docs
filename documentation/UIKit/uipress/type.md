# type

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The type of the specified press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var type: UIPress.PressType { get }
```

```objc
@property (nonatomic, readonly) UIPressType type;
```

## Discussion

For a list of all possible types, see the [`UIPress.PressType`](./presstype.md) enumeration.

## See Also

### Getting press attributes
- [var key: UIKey?](./key.md)
  The key pressed or released on a physical keyboard.
- [var phase: UIPress.Phase](./phase-swift.property.md)
  The current press phase of the object.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when the press occurred or when it was last mutated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/type)*