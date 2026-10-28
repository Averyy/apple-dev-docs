# open(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Opens the location at the specified URL.

**Availability**:
- macOS

## Declaration

```swift
func open(_ url: URL) -> Bool
```

```objc
- (BOOL) openURL:(NSURL *) url;
```

## Return Value

[`true`](../../Swift/true.md) if the location was successfully opened; otherwise, [`false`](../../Swift/false.md).

## Discussion

You can call this method safely from any thread in macOS 10.6 and later.

## Parameters

- `url`: A URL specifying the location to open.

## See Also

### Opening URLs
- [func open(URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](./open%28_,configuration,completionhandler%29.md)
  Opens a URL asynchronously using the provided options.
- [func open([URL], withApplicationAt: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](./open%28_,withapplicationat,configuration,completionhandler%29.md)
  Opens one or more URLs asynchronously in the specified app using the provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/open(_:))*