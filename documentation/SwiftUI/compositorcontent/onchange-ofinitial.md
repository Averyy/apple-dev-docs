# onChange(of:initial:_:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping () -> Void) -> some CompositorContent where V : Equatable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/onchange(of:initial:_:))*