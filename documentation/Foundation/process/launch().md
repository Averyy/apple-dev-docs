# launch()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Launches the task represented by the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use [`run()`](./run%28%29.md) instead.

## Declaration

```swift
func launch()
```

```objc
- (void) launch;
```

## Discussion

Raises an `NSInvalidArgumentException` if the launch path has not been set or is invalid or if it fails to create a process.

## See Also

### Related Documentation
- [func waitUntilExit()](./waituntilexit%28%29.md)
  Blocks the process until the receiver is finished.
- [func terminate()](./terminate%28%29.md)
  Sends a terminate signal to the receiver and all of its subtasks.
### Deprecated
- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](./launchedprocess%28launchpath,arguments%29.md)
  Creates and launches a task with a specified executable and arguments.
- [var currentDirectoryPath: String](./currentdirectorypath.md)
  Sets the current directory for the receiver.
- [var launchPath: String?](./launchpath.md)
  Sets the receiver’s executable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/launch())*