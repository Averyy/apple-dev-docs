# launch()

**Framework**: Foundation  
**Kind**: method

Launches the task represented by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func launch()
```

#### Discussion

Raises an `NSInvalidArgumentException` if the launch path has not been set or is invalid or if it fails to create a process.

## See Also

- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](process/launchedprocess(launchpath:arguments:).md)
  Creates and launches a task with a specified executable and arguments.
- [var currentDirectoryPath: String](process/currentdirectorypath.md)
  Sets the current directory for the receiver.
- [var launchPath: String?](process/launchpath.md)
  Sets the receiver’s executable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/launch())*