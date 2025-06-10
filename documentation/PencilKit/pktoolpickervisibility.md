# PKToolPickerVisibility

**Framework**: PencilKit  
**Kind**: enum

The visibility state of a tool picker.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum PKToolPickerVisibility
```

## Topics

### Enumeration Cases
- [PKToolPickerVisibility.hidden](pktoolpickervisibility/hidden.md)
  Tool picker is active but offscreen, and can appear temporarily in response to user actions.
- [PKToolPickerVisibility.inactive](pktoolpickervisibility/inactive.md)
  No active tool picker.
- [PKToolPickerVisibility.visible](pktoolpickervisibility/visible.md)
  Tool picker is active and onscreen.
### Initializers
- [init?(rawValue: Int)](pktoolpickervisibility/init(rawvalue:).md)
### Instance Methods
- [func toggle()](pktoolpickervisibility/toggle.md)
  Toggles between hidden / visible.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickervisibility)*