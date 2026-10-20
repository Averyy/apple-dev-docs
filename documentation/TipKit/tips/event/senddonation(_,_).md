# sendDonation(_:_:)

**Framework**: TipKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously donates an event along with its associated `Donation` value.

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
func sendDonation(_ donation: DonationInfo, _ completion: (@Sendable () -> Void)? = nil)
```

Available when `DonationInfo` conforms to `Decodable`, `Encodable`, and `Sendable`.

## Parameters

- `donation`: Associated donation value.
- `completion`: Called upon completion of the event donation.

## See Also

### Add Donations
- [func donate() async](./donate%28%29.md)
  Donates an event with no associated `Donation` value.
- [func donate(DonationInfo) async](./donate%28_%29.md)
  Donates an event along with its associated `Donation` value.
- [func sendDonation((() -> Void)?)](./senddonation%28_%29.md)
  Asynchronously donates an event with no associated `Donation` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/event/senddonation(_:_:))*