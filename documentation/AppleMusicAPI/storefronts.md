# Storefronts

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Storefronts
```

#### Discussion

For the specification of language tags, see [`Language Codes`](https://developer.apple.comhttps://help.apple.com/itc/musicspec/?lang=en#/itc740f60829) in iTunes Package Music Specification.

## Topics

### Related Objects
- [object Storefronts.Attributes](storefronts/attributes-data.dictionary.md)
  The attributes for the storefronts resource.

## Properties

- `id` (string) *(required)*: The identifier for the storefront.
- `type` (string) *(required)*: This value must always be `storefronts`.
- `href` (string) *(required)*: The relative location for the storefront resource.
- `attributes` (Storefronts.Attributes): The attributes for the storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/storefronts)*