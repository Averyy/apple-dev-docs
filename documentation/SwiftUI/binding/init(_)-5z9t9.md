# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a binding by projecting the base value to an unwrapped value.

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
init?(_ base: Binding<Value?>)
```

**Other overloads**:

```swift
init<V>(_ base: Binding<V>) where Value == AnyHashable, V : Hashable
```

```swift
init<V>(_ base: Binding<V>) where Value == V?
```

## Return Value

A new binding or `nil` when `base` is `nil`.

## Discussion

> ⚠️ **Warning**: The new binding force-unwraps the value from the original binding. After creating of this binding, the original binding becoming `nil` will result in a crash from the new binding.

## Parameters

- `base`: A value to project to an unwrapped value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/init(_:)-5z9t9)*