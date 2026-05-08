# constant(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a binding with an immutable value.

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
static func constant(_ value: Value) -> Binding<Value>
```

#### Discussion

Use this method to create a binding to a value that cannot change. This can be useful when using a [`PreviewProvider`](previewprovider.md) to see how a view represents different values.

```swift
// Example of binding to an immutable value.
PlayButton(isPlaying: Binding.constant(true))
```

## Parameters

- `value`: An immutable value.

## See Also

- [init(_:)](binding/init(_:).md)
  Creates a binding by projecting the base value to a hashable value.
- [init(projectedValue: Binding<Value>)](binding/init(projectedvalue:).md)
  Creates a binding from the value of another binding.
- [init(get:set:)](binding/init(get:set:).md)
  Creates a binding with closures that read and write the binding value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/constant(_:))*