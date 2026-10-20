# noAutoRename

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the service prohibits automatic renaming in the event of a name conflict.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var noAutoRename: Bool { get set }
```

## See Also

### Defining Services
- [init(name: String?, type: String, domain: String?, txtRecord: Data?)](./init%28name,type,domain,txtrecord%29-1lb30.md)
  Initializes a Bonjour service to advertise.
- [init(name: String?, type: String, domain: String?, txtRecord: NWTXTRecord)](./init%28name,type,domain,txtrecord%29-8qh5.md)
  Initializes a Bonjour service to advertise with a TXT record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/service-swift.struct/noautorename)*