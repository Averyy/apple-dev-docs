# change(for:)

**Framework**: Game Controller  
**Kind**: method  
**Required**: Yes

Returns whether the input value of an element changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func change(for element: any GCPhysicalInputElement) -> GCDevicePhysicalInputElementChange
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Return Value

Description of the change to the element.

## Parameters

- `element`: The element whose value changes.

## See Also

- [enum GCDevicePhysicalInputElementChange](gcdevicephysicalinputelementchange.md)
  Possible values that describe whether the input value of an element changes.
- [func changedElements() -> NSEnumerator?](gcdevicephysicalinputstatediff/changedelements-9cdq4.md)
  Returns the elements that changed since the previous input state.
- [func changedElements() -> (some Sequence<any GCPhysicalInputElement>)?
](gcdevicephysicalinputstatediff/changedelements-2zzwm.md)
  Returns the elements that changed since the previous input state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstatediff/change(for:))*