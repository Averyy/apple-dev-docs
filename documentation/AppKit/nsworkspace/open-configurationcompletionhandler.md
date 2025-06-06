# open(_:configuration:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Opens a URL asynchronously using the provided options.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func open(_ url: URL, configuration: NSWorkspace.OpenConfiguration) async throws -> NSRunningApplication
```

#### Discussion

You may call this method safely from any thread of your app.

## Parameters

- `url`: The URL to open.
- `configuration`: The options that indicate how you want to open the URL.
- `completionHandler`: The completion handler block to call asynchronously with the results. AppKit executes the completion handler on a concurrent queue. The handler block has no return value and takes the following parameters:

## See Also

- [func open([URL], withApplicationAt: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](nsworkspace/open(_:withapplicationat:configuration:completionhandler:).md)
  Opens one or more URLs asynchronously in the specified app using the provided options.
- [func open(URL) -> Bool](nsworkspace/open(_:).md)
  Opens the location at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/open(_:configuration:completionhandler:))*