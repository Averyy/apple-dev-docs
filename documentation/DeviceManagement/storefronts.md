# Storefronts

**Framework**: Device Management  
**Kind**: dictionary

A resource object that represents a region that the content is available in, and supported languages for that region.

**Availability**:
- VPP License Management 2.1+

## Declaration

```swift
object Storefronts
```

## Topics

### Related Objects
- [object Storefronts.Attributes](storefronts/attributes-data.dictionary.md)
  The attributes for the storefronts resource.

## Properties

- `attributes` (Storefronts.Attributes): The attributes for the storefronts resource type.
- `href` (string) *(required)*: A relative location for the storefronts resource.
- `id` (string) *(required)*: The identifier for the storefronts resource.
- `type` (string) *(required)*: The type of the resource. The only allowed value is `storefronts`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/storefronts)*