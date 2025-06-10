# GCDevicePhysicalInputElementChange

**Framework**: Game Controller  
**Kind**: enum

Possible values that describe whether the input value of an element changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum GCDevicePhysicalInputElementChange
```

## Topics

### States
- [GCDevicePhysicalInputElementChange.unknownChange](gcdevicephysicalinputelementchange/unknownchange.md)
  It’s unknown whether there’s a change to the input value.
- [GCDevicePhysicalInputElementChange.noChange](gcdevicephysicalinputelementchange/nochange.md)
  There’s no change to the input value.
- [GCDevicePhysicalInputElementChange.changed](gcdevicephysicalinputelementchange/changed.md)
  There’s a change to the input value.
### Initializers
- [init?(rawValue: Int)](gcdevicephysicalinputelementchange/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func change(for: any GCPhysicalInputElement) -> GCDevicePhysicalInputElementChange](gcdevicephysicalinputstatediff/change(for:).md)
  Returns whether the input value of an element changes.
- [func changedElements() -> NSEnumerator?](gcdevicephysicalinputstatediff/changedelements-9cdq4.md)
  Returns the elements that changed since the previous input state.
- [func changedElements() -> (some Sequence<any GCPhysicalInputElement>)?
](gcdevicephysicalinputstatediff/changedelements-2zzwm.md)
  Returns the elements that changed since the previous input state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputelementchange)*