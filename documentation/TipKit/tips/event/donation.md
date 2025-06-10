# Donation

**Framework**: TipKit  
**Kind**: struct

A repeatable user-defined action.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@dynamicMemberLookup
struct Donation
```

## Topics

### Instance Properties
- [let date: Date](tips/event/donation/date.md)
### Subscripts
- [subscript<Value>(dynamicMember _: KeyPath<DonationInfo, Value>) -> Value](tips/event/donation/subscript(dynamicmember:).md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var donations: [Tips.Event<DonationInfo>.Donation]](tips/event/donations.md)
  Returns an events existing donations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/event/donation)*