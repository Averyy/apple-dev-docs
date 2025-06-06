# launchPath

**Framework**: Foundation  
**Kind**: property

Sets the receiver’s executable.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var launchPath: String? { get set }
```

## Parameters

- `path`: The path to the executable.

## See Also

- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](process/launchedprocess(launchpath:arguments:).md)
  Creates and launches a task with a specified executable and arguments.
- [var currentDirectoryPath: String](process/currentdirectorypath.md)
  Sets the current directory for the receiver.
- [func launch()](process/launch.md)
  Launches the task represented by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/launchpath)*