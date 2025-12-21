# init(identifier:remotePid:)

**Framework**: BrowserEngineKit  
**Kind**: init

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(identifier: String, remotePid: pid_t)
```

#### Discussion

Initializes a remote element in the hosting process.

## Parameters

- `identifier`: Unique identifier to connect this remote element to the remote element it hosts. This should be unique per pair of remote elements.
- `remotePid`: The PID of the hosted remote element’s process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremotehostelement/init(identifier:remotepid:))*