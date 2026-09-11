# directTouch

**Framework**: SwiftUI  
**Kind**: property

A person is touching content directly.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let directTouch: GestureInputKinds
```

#### Discussion

Examples:

- touching a screen directly with fingers,
- directly touching or pinching content in visionOS.

> **Note**: In visionOS, you can further customize what hand motions your gesture recognizes using [`handActivationBehavior(_:)`](gesture/handactivationbehavior(_:).md).

## See Also

- [static let all: GestureInputKinds](gestureinputkinds/all.md)
  All possible gesture input kinds, present and future.
- [static let indirectTouch: GestureInputKinds](gestureinputkinds/indirecttouch.md)
  A person is touching content indirectly.
- [static let pencil: GestureInputKinds](gestureinputkinds/pencil.md)
  A person is touching content directly with an Apple Pencil, or an other supported pencil device.
- [static let pointer: GestureInputKinds](gestureinputkinds/pointer.md)
  A person is pressing a mouse or a trackpad button while the pointer is pointing at content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gestureinputkinds/directtouch)*