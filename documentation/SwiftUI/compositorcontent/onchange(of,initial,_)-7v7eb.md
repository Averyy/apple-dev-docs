# onChange(of:initial:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping (V, V) -> Void) -> some CompositorContent where V : Equatable
```

**Other overloads**:

```swift
nonisolated
func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping () -> Void) -> some CompositorContent where V : Equatable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/onchange(of:initial:_:)-7v7eb)*