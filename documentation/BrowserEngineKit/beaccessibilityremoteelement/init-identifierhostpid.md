# init(identifier:hostPid:)

**Framework**: BrowserEngineKit  
**Kind**: init

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(identifier: String, hostPid: pid_t)
```

#### Discussion

Initializes and registers a remote element. This element doesn’t need to be returned anywhere.

## Parameters

- `identifier`: Unique identifier to connect this remote element to the hosting remote element. This should be unique per pair of remote elements.
- `hostPid`: The PID of the host’s remote element process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremoteelement/init(identifier:hostpid:))*