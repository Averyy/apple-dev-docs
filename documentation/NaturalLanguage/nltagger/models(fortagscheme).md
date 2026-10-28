# models(forTagScheme:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Returns the models that apply to the given tag scheme.

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
func models(forTagScheme tagScheme: NLTagScheme) -> [NLModel]
```

```objc
- (NSArray<NLModel *> *) modelsForTagScheme:(NLTagScheme) tagScheme;
```

## Return Value

The array of models that apply to the given tag scheme.

## Parameters

- `tagScheme`: The tag scheme to filter the list of models with.

## See Also

### Using models with a tagger
- [func setModels([NLModel], forTagScheme: NLTagScheme)](./setmodels%28_,fortagscheme%29.md)
  Assigns models for a tag scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/models(fortagscheme:))*