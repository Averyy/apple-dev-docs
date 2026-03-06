# Relationship

**Framework**: Apple Music API  
**Kind**: dictionary

A to-one or to-many relationship from one resource object to others.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Relationship
```

#### Discussion

A to-one relationship contains a single object in the `data` array.

The rules that apply to the members of this object are:

- Must contain one of these members: `href`, `data`, or `meta`.
- If a to-many relationship, may contain the `next` member.

## Topics

### Related Objects
- [object Relationship.Meta](relationship/meta-data.dictionary.md)
  Information about the request or response.

## Properties

- `href` (string): A URL subpath that fetches the relationship resources as the primary object. This member is only present in responses.
- `next` (string): Link to the next page of resources in the relationship. Contains the `offset` query parameter that specifies the next page. See `Fetch Resources by Page`.
- `data` ([Resource]) *(required)*: One or more destination objects.
- `meta` (Relationship.Meta): Contextual information about the relationship for the request or response.

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/relationship)*