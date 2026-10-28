# Generable(description:representNilExplicitlyInGeneratedContent:)

**Framework**: Foundation Models  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+
- watchOS 27.0+

## Declaration

```swift
@attached(extension, conformances: Generable, names: named(init(_:)), named(generatedContent))
@attached(member, names: arbitrary) macro Generable(description: String? = nil, representNilExplicitlyInGeneratedContent: Bool)
```

## See Also

### Creating a Generable type
- [macro Generable(description: String?)](./generable%28description%29.md)
- [macro Generable(name: String, description: String?, representNilExplicitlyInGeneratedContent: Bool)](./generable%28name,description,representnilexplicitlyingeneratedcontent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(description:representnilexplicitlyingeneratedcontent:))*