# LanguageModelSession.DynamicProfileModifier.DynamicProfile

**Framework**: Foundation Models  
**Kind**: typealias  
**Role**: Type Alias

The dynamic profile type that a modifier’s body returns.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
typealias DynamicProfile = LanguageModelSession.DynamicProfile
```

## See Also

### Implementing a profile modifier
- [func body(content: Self.Content) -> Self.Body](./body%28content%29.md)
  The content of the dynamic profile modifier.
- [LanguageModelSession.DynamicProfileModifier.Content](./content.md)
  The type of dynamic profile content that this modifier wraps.
- [associatedtype Body : LanguageModelSession.DynamicProfile](./body.md)
  The type of dynamic profile modifier that represents this modifier.
- [LanguageModelSession.DynamicProfileModifier.SessionProperty](./sessionproperty.md)
  A property wrapper that provides access to a session property from within a dynamic profile modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofilemodifier/dynamicprofile)*