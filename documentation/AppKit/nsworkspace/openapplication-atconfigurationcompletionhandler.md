# openApplication(at:configuration:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Launches the app at the specified URL and asynchronously reports back on the app’s status.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func openApplication(at applicationURL: URL, configuration: NSWorkspace.OpenConfiguration) async throws -> NSRunningApplication
```

#### Discussion

## Parameters

- `applicationURL`: A URL specifying the location of the app in the file system.
- `configuration`: The options that indicate how you want to launch the app.
- `completionHandler`: The completion handler block to call asynchronously with the results. AppKit executes the completion handler on a concurrent queue. The handler block has no return value and takes the following parameters:

## See Also

- [func hideOtherApplications()](nsworkspace/hideotherapplications.md)
  Hides all applications other than the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openapplication(at:configuration:completionhandler:))*