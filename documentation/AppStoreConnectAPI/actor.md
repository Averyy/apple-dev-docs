# Actor

**Framework**: App Store Connect API  
**Kind**: dictionary

An entity in the audit log representing the person, service, or system that performed an action in App Store Connect.

**Availability**:
- App Store Connect API 2.4+

## Declaration

```swift
object Actor
```

## Topics

### Objects
- [object Actor.Attributes](actor/attributes-data.dictionary.md)
  Attributes that describe an actor resource.

## Properties

- `attributes` (Actor.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [object ActorResponse](actorresponse.md)
  A response containing a single audit log actor who performed a tracked action in App Store Connect.
- [object ActorsResponse](actorsresponse.md)
  A response containing a list of audit log actors who performed actions in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/actor)*