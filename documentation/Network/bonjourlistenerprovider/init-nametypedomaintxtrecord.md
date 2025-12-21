# init(name:type:domain:txtRecord:)

**Framework**: Network  
**Kind**: init

Create a Bonjour service to advertise.

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
init(name: String? = nil, type: String, domain: String? = nil, txtRecord: NWTXTRecord? = nil)
```

#### Discussion

> **Note**: You can use `.bonjour()` as a convenience initializer.

Advertised services should be registered with IANA.

## Parameters

- `name`: The name to advertise. Defaults to  , which allows the system to provide the name.
- `type`: The Bonjour service type to advertise.
- `domain`: The domain to advertise. Defaults to  , which allows Bonjour to register in all default registration domains.
- `txtRecord`: An optional text record to advertise. If not provided, Bonjour will not register   any text record associated with this service. Later, a text record can be advertised by setting   on    with a TXT record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/bonjourlistenerprovider/init(name:type:domain:txtrecord:))*