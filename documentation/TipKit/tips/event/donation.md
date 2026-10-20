# Donation

**Framework**: TipKit  
**Kind**: struct  
**Role**: Structure

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

Available when `DonationInfo` conforms to `Decodable`, `Encodable`, and `Sendable`.

## Topics

### Instance Properties
- [let date: Date](./donation/date.md)
### Subscripts
- [subscript<Value>(dynamicMember _: KeyPath<DonationInfo, Value>) -> Value](./donation/subscript%28dynamicmember%29.md)

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Donations
- [var donations: [Tips.Event<DonationInfo>.Donation]](./donations.md)
  Returns an events existing donations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/event/donation)*