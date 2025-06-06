# init(bundleIdentifier:onInterruption:)

**Framework**: BrowserEngineKit  
**Kind**: init

Launches a web content process asynchronously.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
init(bundleIdentifier: String? = nil, onInterruption: @escaping () -> Void) async throws
```

#### Overview

Initializing a `WebContentProcess` object launches a new instance of the web content extension. The operating system guarantees that the process launched when this initializer returns.

## Parameters

- `bundleIdentifier`: The bundle identifier of the content extension to launch, or   to use the default bundle identifier for this app’s web content extension.
- `onInterruption`: A block that the operating system calls if the web content extension process exits abnormally.

## See Also

- [func invalidate()](webcontentprocess/invalidate.md)
  Stops the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentprocess/init(bundleidentifier:oninterruption:))*