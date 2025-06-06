# launchedProcess(launchPath:arguments:)

**Framework**: Foundation  
**Kind**: method

Creates and launches a task with a specified executable and arguments.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func launchedProcess(launchPath path: String, arguments: [String]) -> Process
```

#### Return Value

An initialized `NSTask` object with the supplied `arguments`.

#### Discussion

The task inherits its environment from the process that invokes this method.

The `NSTask` object converts both `path` and the strings in `arguments` to appropriate C-style strings (using [`fileSystemRepresentation`](nsstring/filesystemrepresentation.md)) before passing them to the task via `argv[])` . The strings in `arguments` don’t undergo shell expansion, so you don’t need to do special quoting, and shell variables, such as `$PWD`, aren’t resolved.

## Parameters

- `path`: The path to the executable.
- `arguments`: An array of   objects that supplies the arguments to the task. If   is  , an   is raised.

## See Also

- [init()](process/init.md)
  Returns an initialized process object with the environment of the current process.
- [var currentDirectoryPath: String](process/currentdirectorypath.md)
  Sets the current directory for the receiver.
- [var launchPath: String?](process/launchpath.md)
  Sets the receiver’s executable.
- [func launch()](process/launch.md)
  Launches the task represented by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/launchedprocess(launchpath:arguments:))*