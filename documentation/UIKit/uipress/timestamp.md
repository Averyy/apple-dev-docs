# timestamp

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The time when the press occurred or when it was last mutated.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval timestamp;
```

#### Discussion

The value of this property is the time, in seconds, from system startup to the time in which the touch either originated or was last changed. You can store and compare the initial value of this attribute to subsequent timestamp values of a [`UIPress`](../uipress.md) instance to determine the duration of the press and, if it’s being swiped, the speed of movement. For a definition of the time-since-boot value, see the description of the [`ProcessInfo`](../../Foundation/processinfo.md) class’s [`systemUptime`](../../Foundation/processinfo/systemuptime.md) method.

## See Also

### Getting press attributes
- [var key: UIKey?](./key.md)
  The key pressed or released on a physical keyboard.
- [var type: UIPress.PressType](./type.md)
  The type of the specified press.
- [var phase: UIPress.Phase](./phase-swift.property.md)
  The current press phase of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/timestamp)*