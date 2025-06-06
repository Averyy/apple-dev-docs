# open(_:)

**Framework**: AppKit  
**Kind**: method

Opens the location at the specified URL.

**Availability**:
- macOS ?+

## Declaration

```swift
func open(_ url: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the location was successfully opened; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You can call this method safely from any thread in macOS 10.6 and later.

## Parameters

- `url`: A URL specifying the location to open.

## See Also

- [func open(URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](nsworkspace/open(_:configuration:completionhandler:).md)
  Opens a URL asynchronously using the provided options.
- [func open([URL], withApplicationAt: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](nsworkspace/open(_:withapplicationat:configuration:completionhandler:).md)
  Opens one or more URLs asynchronously in the specified app using the provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/open(_:))*