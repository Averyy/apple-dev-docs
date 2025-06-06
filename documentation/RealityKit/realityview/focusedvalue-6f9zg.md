# focusedValue(_:_:)

**Framework**: RealityKit  
**Kind**: method

Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func focusedValue<Value>(_ keyPath: WritableKeyPath<FocusedValues, Value?>, _ value: Value) -> some View
```

#### Return Value

A modified representation of this view.

## Parameters

- `keyPath`: The key path to associate   with when adding   it to the existing table of exported focus values.
- `value`: The focus value to export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/focusedvalue(_:_:)-6f9zg)*