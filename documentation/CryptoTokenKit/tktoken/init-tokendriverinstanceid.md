# init(tokenDriver:instanceID:)

**Framework**: CryptoTokenKit  
**Kind**: init

Initializes a token with the driver you specify.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(tokenDriver: TKTokenDriver, instanceID: TKToken.InstanceID)
```

#### Return Value

A new token object.

#### Discussion

This is the designated initializer.

## Parameters

- `tokenDriver`: The driver of the token.
- `instanceID`: A unique, persistent identifier for this token. This value is typically generated from the serial number of the target hardware.

## See Also

- [typealias InstanceID](tktoken/instanceid.md)
  A type that represents the instance identifier of a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/init(tokendriver:instanceid:))*