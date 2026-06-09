# Relationship

**Framework**: Device Management  
**Kind**: dictionary

A to-one or to-many relationship from one resource object to others.

**Availability**:
- VPP License Management 2.1+

## Declaration

```swift
object Relationship
```

## Topics

### Related Objects
- [object Relationship.Meta](relationship/meta-data.dictionary.md)

## Properties

- `data` ([Resource]) *(required)*: A paginated collection of resources in the relationship.
- `href` (string): A relative location to fetch the relationship, if it may be fetched directly.
- `meta` (Relationship.Meta): Contextual data about the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.

## See Also

- [object Resource](resource.md)
  A resource such as an app or book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/relationship)*