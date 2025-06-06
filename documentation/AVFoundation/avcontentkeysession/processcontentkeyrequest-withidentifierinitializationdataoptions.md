# processContentKeyRequest(withIdentifier:initializationData:options:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate to start loading the content decryption key with the specified identifier and initialization data.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func processContentKeyRequest(withIdentifier identifier: (any Sendable)?, initializationData: Data?, options: [String : any Sendable]? = nil)
```

#### Discussion

Either the `identifier` or `initializationData` parameters must be non-`nil`. If required by the protocol, both parameters can be non-`nil`.

## Parameters

- `identifier`: The container- and protocol-specific identifier used to obtain a key response.
- `initializationData`: The container- and protocol-specific data used to obtain a key response.
- `options`: No options are currently defined. Set this value to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/processcontentkeyrequest(withidentifier:initializationdata:options:))*