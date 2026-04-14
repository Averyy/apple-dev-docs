# init(identifier:hostPid:)

**Framework**: BrowserEngineKit  
**Kind**: init

Initializes and registers a remote element.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(identifier: String, hostPid: pid_t)
```

#### Discussion

Don’t return an instance of this class from an object in your view hierarchy.

## Parameters

- `identifier`: A unique ID that creates an element reference pair by connecting an accessibility element to its representation that the local process hosts. Set this parameter to a unique value per pair of element references.
- `hostPid`: The process ID of the host’s remote element process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremoteelement/init(identifier:hostpid:))*