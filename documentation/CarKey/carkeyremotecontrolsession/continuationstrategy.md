# CarKeyRemoteControlSession.ContinuationStrategy

**Framework**: CarKey  
**Kind**: enum  
**Role**: Enumeration

Strategy to use on reception of a continuation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
enum ContinuationStrategy
```

## Topics

### Enumeration Cases
- [CarKeyRemoteControlSession.ContinuationStrategy.automatic](./continuationstrategy/automatic.md)
  Auto-confirm any incoming continuation requests until the requested action is stopped or completed with no intervention from the client.
- [CarKeyRemoteControlSession.ContinuationStrategy.manual](./continuationstrategy/manual.md)
  Give your app control over the incoming continuation requests and allow to exchange data with the vehicle.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/continuationstrategy)*