# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript

Reads and writes values associated with a given focused value key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
subscript<Key>(key: Key.Type) -> Key.Value? where Key : FocusedValueKey { get set }
```

#### Overview

Use this subscript to get or set a focused value for a custom [`FocusedValueKey`](focusedvaluekey.md). In most cases, you’ll use the `Entry` macro to create focused value properties, which automatically generates the appropriate key and uses this subscript internally:

```swift
extension FocusedValues {
    @Entry var myCustomValue: MyType?
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedvalues/subscript(_:))*