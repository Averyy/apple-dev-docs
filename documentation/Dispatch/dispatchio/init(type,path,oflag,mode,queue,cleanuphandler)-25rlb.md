# init(type:path:oflag:mode:queue:cleanupHandler:)

**Framework**: Dispatch  
**Kind**: init

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
convenience init(type: DispatchIO.StreamType, path: UnsafePointer<Int8>, oflag: Int32, mode: mode_t, queue: DispatchQueue, cleanupHandler: @escaping (Int32) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-25rlb)*