# init(bundleIdentifier:onInterruption:)

**Framework**: BrowserEngineKit  
**Kind**: init

Launches a rendering extension process asynchronously.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
init(bundleIdentifier: String? = nil, onInterruption: @escaping () -> Void) async throws
```

#### Overview

Your web browser app can run one instance of each of its rendering extensions. The first time you initialize this object, the operating system launches your rendering extension. If you subsequently initialize new instances of `RenderingProcess` using the same bundle identifier, they refer to the same process.

The operating system guarantees that the process launched when this initializer returns.

## Parameters

- `bundleIdentifier`: The bundle identifier of the rendering extension to launch, or   to use the default bundle identifier for this app’s rendering extension.
- `onInterruption`: A block that the operating system calls if the rendering extension process exits abnormally.

## See Also

- [func invalidate()](renderingprocess/invalidate.md)
  Stops the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess/init(bundleidentifier:oninterruption:))*