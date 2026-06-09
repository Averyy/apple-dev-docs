# prependApplicationProtocolIgnoringReady(options:)

**Framework**: Network  
**Kind**: method

Dynamically add a protocol to a connection establishment attempt “above” the framer protocol. This means that the protocol above will start running once the framer becomes ready by calling markReady(). This can only be used with framers that return a value of willMarkReady to their start handlers. An example of using this functionality is adding a security protocol, like TLS, above a framer once that framer completes its initial handshake.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final func prependApplicationProtocolIgnoringReady(options: NWProtocolOptions) throws
```

#### Discussion

To ensure thread safety, this function can only be called in one of the callback blocks invoked on the framer, or in a block passed to NWProtocolFramer.Instance.async().

Throws an error if the protocol could not be added.

This function differs from prependApplicationProtocol when the framer has already been marked ready. prependApplicationProtocol will throw an error if the framer was marked ready. prependApplicationProtocolIgnoringReady will still add the protocol and reset ready. The framer must markReady again.

If there is data in-flight on the connection, the behavior is undefined.

## Parameters

- `options`: Protocol options for an application protocol to dynamically add “above” the framer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/prependapplicationprotocolignoringready(options:))*