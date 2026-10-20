# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the environment value associated with a custom key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
subscript<K>(key: K.Type) -> K.Value where K : EnvironmentKey { get set }
```

**Other overloads**:

```swift
subscript<K>(key: K.Type) -> K.Value where K : UITraitBridgedEnvironmentKey { get set }
```

```swift
subscript<T>(objectType: T.Type) -> T? where T : AnyObject, T : Observable { get set }
```

#### Overview

Create a custom environment value by declaring a new property in an extension to the environment values structure and applying the [`Entry()`](../entry%28%29.md) macro to the variable declaration:

```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
}
```

You use custom environment values the same way you use system-provided values, setting a value with the [`environment(_:_:)`](../view/environment%28_,_%29.md) view modifier, and reading values with the [`Environment`](../environment.md) property wrapper. You can also provide a dedicated view modifier as a convenience for setting the value:

```swift
extension View {
    func myCustomValue(_ myCustomValue: String) -> some View {
        environment(\.myCustomValue, myCustomValue)
    }
}
```

## See Also

### Creating and accessing values
- [init()](./init%28%29.md)
  Creates an environment values instance.
- [var description: String](./description.md)
  A string that represents the contents of the environment values instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/subscript(_:))*