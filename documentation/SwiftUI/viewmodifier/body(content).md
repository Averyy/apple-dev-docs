# body(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the current body of the caller.

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
@ContentBuilder
@MainActor @preconcurrency func body(content: Self.Content) -> Self.Body
```

## Discussion

`content` is a proxy for the view that will have the modifier represented by `Self` applied to it.

## Default Implementations

### ViewModifier Implementations
- [func body(content: Self.Content) -> Self.Body](./body%28content%29-70h6f.md)
  Gets the current body of the caller.

## See Also

### Creating a view modifier
- [associatedtype Body : View](./body.md)
  The type of view representing the body.
- [ViewModifier.Content](./content.md)
  The content view type passed to `body()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewmodifier/body(content:))*