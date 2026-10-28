# currentDirectoryPath

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the current directory for the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use [`currentDirectoryURL`](./currentdirectoryurl.md) instead.

## Declaration

```swift
var currentDirectoryPath: String { get set }
```

```objc
@property (copy) NSString * currentDirectoryPath;
```

## Discussion

If this method isn’t used, the current directory is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the receiver has already been launched.

## Parameters

- `path`: The current directory for the task.

## See Also

### Deprecated
- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](./launchedprocess%28launchpath,arguments%29.md)
  Creates and launches a task with a specified executable and arguments.
- [var launchPath: String?](./launchpath.md)
  Sets the receiver’s executable.
- [func launch()](./launch%28%29.md)
  Launches the task represented by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/currentdirectorypath)*