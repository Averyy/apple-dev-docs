# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a binding by projecting the base value to a hashable value.

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
init<V>(_ base: Binding<V>) where Value == AnyHashable, V : Hashable
```

**Other overloads**:

```swift
init<V>(_ base: Binding<V>) where Value == V?
```

```swift
init?(_ base: Binding<Value?>)
```

## Parameters

- `base`: A `Hashable` value to project to an `AnyHashable` value.

## See Also

### Creating a binding
- [init(projectedValue: Binding<Value>)](./init%28projectedvalue%29.md)
  Creates a binding from the value of another binding.
- [init(get:set:)](./init%28get,set%29.md)
  Creates a binding with closures that read and write the binding value.
- [static func constant(Value) -> Binding<Value>](./constant%28_%29.md)
  Creates a binding with an immutable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/init(_:))*