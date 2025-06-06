# donate(_:)

**Framework**: TipKit  
**Kind**: method

Donates an event along with its associated `Donation` value.

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
func donate(_ donation: DonationInfo) async
```

## Parameters

- `donation`: Associated donation value.

## See Also

- [func donate() async](tips/event/donate.md)
  Donates an event with no associated `Donation` value.
- [func sendDonation((() -> Void)?)](tips/event/senddonation(_:).md)
  Asynchronously donates an event with no associated `Donation` value.
- [func sendDonation(DonationInfo, (() -> Void)?)](tips/event/senddonation(_:_:).md)
  Asynchronously donates an event along with its associated `Donation` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/event/donate(_:))*