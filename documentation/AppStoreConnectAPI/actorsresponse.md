# ActorsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a list of audit log actors who performed actions in App Store Connect.

**Availability**:
- App Store Connect API 2.4+

## Declaration

```
object ActorsResponse
```

## Properties

- `data` ([Actor]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object Actor](./actor.md)
  An entity in the audit log representing the person, service, or system that performed an action in App Store Connect.
- [object ActorResponse](./actorresponse.md)
  A response containing a single audit log actor who performed a tracked action in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/actorsresponse)*