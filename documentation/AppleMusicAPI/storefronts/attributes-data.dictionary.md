# Storefronts.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The attributes for the storefronts resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Storefronts.Attributes
```

## Properties

- `defaultLanguageTag` (string) *(required)*: The default supported RFC4646 language tag for the storefront.
- `explicitContentPolicy` (string) *(required)*: Attribute indicating the level that this storefront can display explicit content.

  **Allowed Values**: `allowed`, `opt-in`, `prohibited`
- `name` (string) *(required)*: The localized name of the storefront.
- `supportedLanguageTags` ([string]) *(required)*: The supported RFC4646 language tags for the storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/storefronts/attributes-data.dictionary)*