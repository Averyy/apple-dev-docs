# init(code:reason:)

**Framework**: Network  
**Kind**: init

Initializes a QUIC application error with an error code and an optional reason.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(code: UInt64, reason: String? = nil)
```

## Parameters

- `code`: The error code.
- `reason`: A string that describes the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/applicationerror/init(code:reason:))*