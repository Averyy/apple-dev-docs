# version(_:)

**Framework**: Network  
**Kind**: method

Specify a single version of the Internet Protocol to allow.

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
func version(_ version: NWProtocolIP.Options.Version) -> IP
```

#### Discussion

Setting this value will constrain which address endpoints can be used and will filter DNS results during connection establishment.

## Parameters

- `version`: The IP version, IPv4 or IPv6.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ip/version(_:))*