# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a binding by projecting the base value to an optional value.

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
init<V>(_ base: Binding<V>) where Value == V?
```

**Other overloads**:

```swift
init<V>(_ base: Binding<V>) where Value == AnyHashable, V : Hashable
```

```swift
init?(_ base: Binding<Value?>)
```

## Parameters

- `base`: A value to project to an optional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/init(_:)-6krsi)*