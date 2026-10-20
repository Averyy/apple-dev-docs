# launchPath

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the receiver’s executable.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use [`executableURL`](./executableurl.md) instead.

## Declaration

```swift
var launchPath: String? { get set }
```

```objc
@property (copy, nullable) NSString * launchPath;
```

## Parameters

- `path`: The path to the executable.

## See Also

### Deprecated
- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](./launchedprocess%28launchpath,arguments%29.md)
  Creates and launches a task with a specified executable and arguments.
- [var currentDirectoryPath: String](./currentdirectorypath.md)
  Sets the current directory for the receiver.
- [func launch()](./launch%28%29.md)
  Launches the task represented by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/launchpath)*