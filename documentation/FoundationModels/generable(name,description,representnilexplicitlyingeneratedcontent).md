# Generable(name:description:representNilExplicitlyInGeneratedContent:)

**Framework**: Foundation Models  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@attached(extension, conformances: Generable, names: named(init(_:)), named(generatedContent))
@attached(member, names: arbitrary) macro Generable(name: String, description: String? = nil, representNilExplicitlyInGeneratedContent: Bool = false)
```

## See Also

### Creating a Generable type
- [macro Generable(description: String?)](./generable%28description%29.md)
- [macro Generable(description: String?, representNilExplicitlyInGeneratedContent: Bool)](./generable%28description,representnilexplicitlyingeneratedcontent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(name:description:representnilexplicitlyingeneratedcontent:))*