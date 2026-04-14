# init(identifier:remotePid:)

**Framework**: BrowserEngineKit  
**Kind**: init

Initializes a remote element in the hosting process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(identifier: String, remotePid: pid_t)
```

## Parameters

- `identifier`: A unique ID that connects a remote element to its hosted version in the local process. Set this parameter to a unique value per pair of element references.
- `remotePid`: The process ID for the hosted remote element’s process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremotehostelement/init(identifier:remotepid:))*