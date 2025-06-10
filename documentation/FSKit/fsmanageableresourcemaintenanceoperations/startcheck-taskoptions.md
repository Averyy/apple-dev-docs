# startCheck(task:options:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Starts checking the file system with the given options.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func startCheck(task: FSTask, options: FSTaskOptions) throws -> Progress
```

#### Return Value

An [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) object that you use to update progress as the check operation progresses. Return `nil` if starting the file system check encountered an error.

## Parameters

- `task`: A task object you use to communicate back to the client.
- `options`: Options for performing the check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmanageableresourcemaintenanceoperations/startcheck(task:options:))*