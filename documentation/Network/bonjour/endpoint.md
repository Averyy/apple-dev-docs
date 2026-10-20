# Bonjour.Endpoint

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

An endpoint for a discovered Bonjour service.

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
struct Endpoint
```

## Topics

### Operators
- [static func == (Bonjour.Endpoint, Bonjour.Endpoint) -> Bool](./endpoint/eqeq%28_,_%29.md)
  Compare two endpoints for equality.
### Instance Properties
- [var description: String](./endpoint/description.md)
  A description of this endpoint to be used for logging and debugging purposes.
- [let domain: String](./endpoint/domain.md)
  The Bonjour domain of the endpoint.
- [var id: String](./endpoint/id.md)
  A unique identifer for the endpoint.
- [let name: String](./endpoint/name.md)
  The Bonjour name of the endpoint.
- [var nwEndpoint: NWEndpoint](./endpoint/nwendpoint.md)
  The NWEndpoint to use when connecting to this result.
- [let result: NWBrowser.Result](./endpoint/result.md)
  A snapshot of the endpoint at some point in time on the network.
- [let txtRecord: NWTXTRecord](./endpoint/txtrecord.md)
  TXT records provide additional information about an endpoint during advertisement or discovery.
- [let type: String](./endpoint/type.md)
  The Bonjour type of the endpoint.

## Relationships

### Conforms To
- [Connectable](../connectable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/bonjour/endpoint)*