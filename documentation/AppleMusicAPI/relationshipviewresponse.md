# RelationshipViewResponse

**Framework**: Apple Music API  
**Kind**: dictionary

The response for a direct resource view fetch.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object RelationshipViewResponse
```

## Topics

### Related Objects
- [object RelationshipViewResponse.Attributes](relationshipviewresponse/attributes-data.dictionary.md)
  The attribute metadata for the view.
- [object RelationshipViewResponse.Meta](relationshipviewresponse/meta-data.dictionary.md)
  Contextual data about the view.

## Properties

- `attributes` (RelationshipViewResponse.Attributes): The attribute metadata for the view.
- `data` ([Resource]) *(required)*: A paginated collection of resources in the view.
- `meta` (RelationshipViewResponse.Meta): Contextual data about the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/relationshipviewresponse)*