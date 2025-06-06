# EnvironmentKey

**Framework**: SwiftUI  
**Kind**: protocol

A key for accessing values in the environment.

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
protocol EnvironmentKey
```

#### Overview

You can create custom environment values by extending the [`EnvironmentValues`](environmentvalues.md) structure with new properties. First declare a new environment key type and specify a value for the required [`defaultValue`](environmentkey/defaultvalue.md) property:

```swift
private struct MyEnvironmentKey: EnvironmentKey {
    static let defaultValue: String = "Default value"
}
```

The Swift compiler automatically infers the associated [`Value`](environmentkey/value.md) type as the type you specify for the default value. Then use the key to define a new environment value property:

```swift
extension EnvironmentValues {
    var myCustomValue: String {
        get { self[MyEnvironmentKey.self] }
        set { self[MyEnvironmentKey.self] = newValue }
    }
}
```

Clients of your environment value never use the key directly. Instead, they use the key path of your custom environment value property. To set the environment value for a view and all its subviews, add the [`environment(_:_:)`](view/environment(_:_:).md) view modifier to that view:

```swift
MyView()
    .environment(\.myCustomValue, "Another string")
```

As a convenience, you can also define a dedicated view modifier to apply this environment value:

```swift
extension View {
    func myCustomValue(_ myCustomValue: String) -> some View {
        environment(\.myCustomValue, myCustomValue)
    }
}
```

This improves clarity at the call site:

```swift
MyView()
    .myCustomValue("Another string")
```

To read the value from inside `MyView` or one of its descendants, use the [`Environment`](environment.md) property wrapper:

```swift
struct MyView: View {
    @Environment(\.myCustomValue) var customValue: String

    var body: some View {
        Text(customValue) // Displays "Another string".
    }
}
```

## Topics

### Getting the default value
- [static var defaultValue: Self.Value](environmentkey/defaultvalue.md)
  The default value for the environment key.
- [associatedtype Value](environmentkey/value.md)
  The associated type representing the type of the environment key’s value.

## Relationships

### Inherited By
- [UITraitBridgedEnvironmentKey](uitraitbridgedenvironmentkey.md)

## See Also

- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentkey)*