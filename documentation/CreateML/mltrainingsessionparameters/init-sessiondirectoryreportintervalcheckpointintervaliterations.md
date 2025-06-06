# init(sessionDirectory:reportInterval:checkpointInterval:iterations:)

**Framework**: Create ML  
**Kind**: init

Creates a set of parameters for a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(sessionDirectory: URL? = nil, reportInterval: Int = 5, checkpointInterval: Int = 10, iterations: Int = 1000)
```

## Parameters

- `sessionDirectory`: The location in the file system where the session stores its progress.
- `reportInterval`: The number of iterations the session completes before it reports its progress.
- `checkpointInterval`: The number of iterations the session completes before it saves a checkpoint.
- `iterations`: The total number of iterations for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/init(sessiondirectory:reportinterval:checkpointinterval:iterations:))*