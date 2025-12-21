# init(using:_:)

**Framework**: Network  
**Kind**: init

Create a Framer protocol for use in a protocol stack.

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
init<BelowProtocol>(using framer: T.Type, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : MessageProtocol
```

## Parameters

- `builder`: The protocol stack below Framer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/framer/init(using:_:)-94t7p)*