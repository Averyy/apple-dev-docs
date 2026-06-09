# Apps

**Framework**: Device Management  
**Kind**: dictionary

A resource object that represents an app.

**Availability**:
- VPP License Management 2.1+

## Declaration

```swift
object Apps
```

## Topics

### Related Objects
- [object Apps.Attributes](apps/attributes-data.dictionary.md)
  The attributes for an apps resource.
- [object Apps.Relationships](apps/relationships-data.dictionary.md)
  The relationships for an apps resource.

## Properties

- `attributes` (Apps.Attributes): The attributes for the apps resource type.
- `href` (string) *(required)*: A relative location for the apps resource.
- `id` (string) *(required)*: The identifier for the apps resource.
- `relationships` (Apps.Relationships): The relationships from apps to other resources.
- `type` (string) *(required)*: The type of the resource. The only allowed value is `apps`.

## See Also

- [object Artwork](artwork.md)
  An object that represents artwork.
- [object DescriptionAttribute](descriptionattribute.md)
  An object that represents a description attribute.
- [object Genres](genres.md)
  A resource object that represents a music genre.
- [object Books](books.md)
  A resource object that represents a book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apps)*