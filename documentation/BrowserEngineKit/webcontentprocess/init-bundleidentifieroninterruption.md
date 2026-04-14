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

#### Discussion

Initializing a [`WebContentProcess`](webcontentprocess.md) object launches a new instance of a web content extension. Control returns from this method only after the process for the new web content extension launches.

## Parameters

- `bundleIdentifier`: A unique bundle identifier for the content extension, or `nil` to use the default web content extension bundle identifier.
- `onInterruption`: A block that the system calls if the web content extension process ends abruptly.

## See Also

- [func invalidate()](webcontentprocess/invalidate.md)
  Stops the web content process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentprocess/init(bundleidentifier:oninterruption:))*