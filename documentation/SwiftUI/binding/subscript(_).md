# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
subscript<C>(componentType: C.Type) -> Binding<C?> where C : Component { get }
```

Available when `Value` is `Entity.Observable.Components`.

**Other overloads**:

```swift
subscript<C>(componentType: C.Type) -> Binding<C?> where C : _ImplicitlyAnimatableBuiltinComponent { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/subscript(_:))*