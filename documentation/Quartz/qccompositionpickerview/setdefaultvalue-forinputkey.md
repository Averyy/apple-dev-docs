# setDefaultValue(_:forInputKey:)

**Framework**: Quartz  
**Kind**: method

Sets the default value to use for a composition input parameter.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setDefaultValue(_ value: Any!, forInputKey key: String!)
```

## Parameters

- `value`: This default value overrides any initial value existing for composition input parameters with this key. Pass   to clear the default value.
- `key`: The input parameter key whose default value you want to set.

## See Also

- [func resetDefaultInputValues()](qccompositionpickerview/resetdefaultinputvalues.md)
  Clears all previously set default values for composition input parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setdefaultvalue(_:forinputkey:))*