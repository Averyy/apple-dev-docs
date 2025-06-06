# changedElements()

**Framework**: Game Controller  
**Kind**: method

Returns the elements that changed since the previous input state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func changedElements() -> (some Sequence<any GCPhysicalInputElement>)?
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Return Value

A sequence that contains the changed elements in no particular order.

#### Discussion

Returns `nil` if there’s no previous input state, either because this is the first input state or Game Controller discards the prior input state because the queue is full.

## See Also

- [func change(for: any GCPhysicalInputElement) -> GCDevicePhysicalInputElementChange](gcdevicephysicalinputstatediff/change(for:).md)
  Returns whether the input value of an element changes.
- [enum GCDevicePhysicalInputElementChange](gcdevicephysicalinputelementchange.md)
  Possible values that describe whether the input value of an element changes.
- [func changedElements() -> NSEnumerator?](gcdevicephysicalinputstatediff/changedelements-9cdq4.md)
  Returns the elements that changed since the previous input state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstatediff/changedelements()-2zzwm)*