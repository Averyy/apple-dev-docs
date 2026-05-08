# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript

Accesses the particular container value associated with a custom key.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
subscript<Key>(key: Key.Type) -> Key.Value where Key : ContainerValueKey { get set }
```

#### Overview

Create a custom container value by declaring a new property in an extension to the container values structure and applying the [`Entry()`](entry().md) macro to the variable declaration:

```swift
extension ContainerValues {
    @Entry var myCustomValue: String = "Default value"
}
```

You use custom container values the same way you use system-provided values, setting a value with the [`containerValue(_:_:)`](view/containervalue(_:_:).md) view modifier, and reading values from a [`Subview`](subview.md) provided by the `subviews` modifier. You can also provide a dedicated view modifier as a convenience for setting the value:

```swift
extension View {
    func myCustomValue(_ myCustomValue: String) -> some View {
        containerValue(\.myCustomValue, myCustomValue)
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containervalues/subscript(_:))*