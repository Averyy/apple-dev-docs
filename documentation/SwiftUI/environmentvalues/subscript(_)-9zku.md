# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the environment value associated with a custom key.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
subscript<K>(key: K.Type) -> K.Value where K : UITraitBridgedEnvironmentKey { get set }
```

**Other overloads**:

```swift
subscript<K>(key: K.Type) -> K.Value where K : EnvironmentKey { get set }
```

```swift
subscript<T>(objectType: T.Type) -> T? where T : AnyObject, T : Observable { get set }
```

## Overview

Create custom environment values by defining a key that conforms to the [`EnvironmentKey`](../environmentkey.md) protocol, and then using that key with the subscript operator of the [`EnvironmentValues`](../environmentvalues.md) structure to get and set a value for that key:

```swift
private struct MyEnvironmentKey: EnvironmentKey {
    static let defaultValue: String = "Default value"
}

extension EnvironmentValues {
    var myCustomValue: String {
        get { self[MyEnvironmentKey.self] }
        set { self[MyEnvironmentKey.self] = newValue }
    }
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/subscript(_:)-9zku)*