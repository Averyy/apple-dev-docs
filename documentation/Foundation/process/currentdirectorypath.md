# currentDirectoryPath

**Framework**: Foundation  
**Kind**: property

Sets the current directory for the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var currentDirectoryPath: String { get set }
```

#### Discussion

If this method isn’t used, the current directory is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the receiver has already been launched.

## Parameters

- `path`: The current directory for the task.

## See Also

- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](process/launchedprocess(launchpath:arguments:).md)
  Creates and launches a task with a specified executable and arguments.
- [var launchPath: String?](process/launchpath.md)
  Sets the receiver’s executable.
- [func launch()](process/launch.md)
  Launches the task represented by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/currentdirectorypath)*