# init(implementation:)

**Framework**: Network  
**Kind**: init

Initializes a new protocol definition based on your protocol implementation.

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
init(implementation: any NWProtocolFramerImplementation.Type)
```

#### Discussion

Each time you initialize a protocol definition with your implemention, a new definition is created that will not be considered equal to other definitions. If you need to associate messages with a protocol you have added to a connection’s protocol stack, make sure to use the same definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/definition/init(implementation:))*