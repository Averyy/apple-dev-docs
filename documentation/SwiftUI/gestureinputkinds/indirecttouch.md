# indirectTouch

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A person is touching content indirectly.

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
static let indirectTouch: GestureInputKinds
```

#### Discussion

Examples:

- performing a multi-touch gesture on a trackpad’s surface,
- swiping on Siri Remote’s surface in tvOS,
- indirectly pinching content while looking at it in visionOS.

## See Also

### Gesture input options
- [static let all: GestureInputKinds](./all.md)
  All possible gesture input kinds, present and future.
- [static let directTouch: GestureInputKinds](./directtouch.md)
  A person is touching content directly.
- [static let pencil: GestureInputKinds](./pencil.md)
  A person is touching content directly with an Apple Pencil, or an other supported pencil device.
- [static let pointer: GestureInputKinds](./pointer.md)
  A person is pressing a mouse or a trackpad button while the pointer is pointing at content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gestureinputkinds/indirecttouch)*