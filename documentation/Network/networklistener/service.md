# service

**Framework**: Network  
**Kind**: property

An optional service to advertise with the listener.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final var service: NWListener.Service? { get set }
```

#### Discussion

May be modified after the listener becomes ready to update the TXT record or change the advertised service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/service)*