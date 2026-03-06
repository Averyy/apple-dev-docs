# RelationshipResponse

**Framework**: Apple Music API  
**Kind**: dictionary

The response for a direct resource relationship fetch.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object RelationshipResponse
```

## Topics

### Related Objects
- [object RelationshipResponse.Meta](relationshipresponse/meta-data.dictionary.md)
  Contextual data about the relationship.

## Properties

- `data` ([Resource]) *(required)*: A paginated collection of resources in the relationship.
- `meta` (RelationshipResponse.Meta): Contextual data about the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/relationshipresponse)*