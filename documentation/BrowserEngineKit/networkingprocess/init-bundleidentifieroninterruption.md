# init(bundleIdentifier:onInterruption:)

**Framework**: BrowserEngineKit  
**Kind**: init

Launches a networking extension process asynchronously.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
init(bundleIdentifier: String? = nil, onInterruption: @escaping () -> Void) async throws
```

#### Discussion

Your browser app can run one instance of each of its networking extensions. The first time you initialize this object, the system launches your networking extension. If you subsequently initialize new instances of `NetworkingProcess` using the same bundle identifier, they refer to the same process.

The system guarantees that the process launched when this initializer returns.

## Parameters

- `bundleIdentifier`: The bundle identifier of the networking extension to launch, or `nil` to use the default bundle identifier for this app’s networking extension.
- `onInterruption`: A block that the system calls if the networking extension process exits abnormally.

## See Also

- [func invalidate()](networkingprocess/invalidate.md)
  Stops the networking process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingprocess/init(bundleidentifier:oninterruption:))*