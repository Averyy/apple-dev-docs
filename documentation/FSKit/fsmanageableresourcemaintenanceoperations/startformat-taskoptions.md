# startFormat(task:options:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Starts formatting the file system with the given options.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func startFormat(task: FSTask, options: FSTaskOptions) throws -> Progress
```

#### Return Value

An [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) object that you use to update progress as the format operation progresses. Return `nil` if starting to format the file system encountered an error.

## Parameters

- `task`: A task object you use to communicate back to the client.
- `options`: Options for performing the format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmanageableresourcemaintenanceoperations/startformat(task:options:))*