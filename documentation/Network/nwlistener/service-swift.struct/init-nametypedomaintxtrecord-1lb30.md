# init(name:type:domain:txtRecord:)

**Framework**: Network  
**Kind**: init

Initializes a Bonjour service to advertise.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(name: String? = nil, type: String, domain: String? = nil, txtRecord: Data? = nil)
```

#### Discussion

Advertised services are primarily defined by their types. If you do not specify a service name, the device name will be chosen. You should not specify a Bonjour domain unless you know you need to advertise only on a particular domain.

## See Also

- [init(name: String?, type: String, domain: String?, txtRecord: NWTXTRecord)](nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-8qh5.md)
  Initializes a Bonjour service to advertise with a TXT record.
- [var noAutoRename: Bool](nwlistener/service-swift.struct/noautorename.md)
  A Boolean that indicates whether the service prohibits automatic renaming in the event of a name conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-1lb30)*