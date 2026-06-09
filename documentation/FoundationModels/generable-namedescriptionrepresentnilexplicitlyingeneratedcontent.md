# Generable(name:description:representNilExplicitlyInGeneratedContent:)

**Framework**: Foundation Models  
**Kind**: macro

Conforms a type to [`Generable`](generable.md) protocol, using a custom name for the schema instead of the Swift type name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@attached
(extension, conformances: Generable, names: named(init(_:)), named(generatedContent)) @attached(member, names: arbitrary) macro Generable(name: String, description: String? = nil, representNilExplicitlyInGeneratedContent: Bool = false)
```

## See Also

- [macro Generable(description: String?)](generable(description:).md)
  Conforms a type to [`Generable`](generable.md) protocol.
- [macro Generable(description: String?, representNilExplicitlyInGeneratedContent: Bool)](generable(description:representnilexplicitlyingeneratedcontent:).md)
  Conforms a type to [`Generable`](generable.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(name:description:representnilexplicitlyingeneratedcontent:))*