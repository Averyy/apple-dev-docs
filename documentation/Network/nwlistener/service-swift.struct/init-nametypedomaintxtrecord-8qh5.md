# init(name:type:domain:txtRecord:)

**Framework**: Network  
**Kind**: init

Initializes a Bonjour service to advertise with a TXT record.

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
init(name: String? = nil, type: String, domain: String? = nil, txtRecord: NWTXTRecord)
```

#### Discussion

Advertised services are primarily defined by their types. If you do not specify a service name, the device name will be chosen. You should not specify a Bonjour domain unless you know you need to advertise only on a particular domain.

## See Also

- [init(name: String?, type: String, domain: String?, txtRecord: Data?)](nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-1lb30.md)
  Initializes a Bonjour service to advertise.
- [var noAutoRename: Bool](nwlistener/service-swift.struct/noautorename.md)
  A Boolean that indicates whether the service prohibits automatic renaming in the event of a name conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-8qh5)*