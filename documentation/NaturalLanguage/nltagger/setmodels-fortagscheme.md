# setModels(_:forTagScheme:)

**Framework**: Natural Language  
**Kind**: method

Assigns models for a tag scheme.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func setModels(_ models: [NLModel], forTagScheme tagScheme: NLTagScheme)
```

#### Discussion

An array of models is allowed for the case where multiple models need to be used. For example, when models were trained on specific languages.

## Parameters

- `models`: Array of   objects to be used with this tagger.
- `tagScheme`: The tag scheme the models would be used with.

## See Also

- [func models(forTagScheme: NLTagScheme) -> [NLModel]](nltagger/models(fortagscheme:).md)
  Returns the models that apply to the given tag scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/setmodels(_:fortagscheme:))*