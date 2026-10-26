# change(for:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (GCDevicePhysicalInputElementChange) changeForElement:(id<GCPhysicalInputElement>) element;
```

## Mentions

- [Handling input events](../handling-input-events.md)

#### Return Value

Description of the change to the element.

## Parameters

- `element`: The element whose value changes.

## See Also

### Getting changes
- [enum GCDevicePhysicalInputElementChange](../gcdevicephysicalinputelementchange.md)
  Possible values that describe whether the input value of an element changes.
- [func changedElements() -> NSEnumerator?](./changedelements%28%29-9cdq4.md)
  Returns the elements that changed since the previous input state.
- [func changedElements() -> (some Sequence<any GCPhysicalInputElement>)?
](./changedelements%28%29-2zzwm.md)
  Returns the elements that changed since the previous input state.
- [- changedElements](./changedelements.md)
  Returns the elements that changed since the previous input state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstatediff/change(for:))*