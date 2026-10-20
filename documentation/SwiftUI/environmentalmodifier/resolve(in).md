# resolve(in:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Resolve to a concrete modifier in the given `environment`.

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
nonisolated
func resolve(in environment: EnvironmentValues) -> Self.ResolvedModifier
```

## See Also

### Resolving a modifier
- [associatedtype ResolvedModifier : ViewModifier](./resolvedmodifier.md)
  The type of modifier to use after being resolved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentalmodifier/resolve(in:))*