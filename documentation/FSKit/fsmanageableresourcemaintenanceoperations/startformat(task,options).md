# startFormat(task:options:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Starts formatting the file system with the given options.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func startFormat(task: FSTask, options: FSTaskOptions) throws -> Progress
```

```objc
- (NSProgress *) startFormatWithTask:(FSTask *) task options:(FSTaskOptions *) options error:(NSError **) error;
```

## Return Value

An [`Progress`](../../Foundation/progress.md) object that you use to update progress as the format operation progresses. Return `nil` if starting to format the file system encountered an error.

## Parameters

- `task`: A task object you use to communicate back to the client.
- `options`: Options for performing the format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmanageableresourcemaintenanceoperations/startformat(task:options:))*