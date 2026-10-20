# open(_:configuration:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Opens a URL asynchronously using the provided options.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func open(_ url: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: (@Sendable (NSRunningApplication?, (any Error)?) -> Void)? = nil)
```

```swift
func open(_ url: URL, configuration: NSWorkspace.OpenConfiguration) async throws -> NSRunningApplication
```

```objc
- (void) openURL:(NSURL *) url configuration:(NSWorkspaceOpenConfiguration *) configuration completionHandler:(void (^)(NSRunningApplication *app, NSError *error)) completionHandler;
```

#### Discussion

You may call this method safely from any thread of your app.

## Parameters

- `url`: The URL to open.
- `configuration`: The options that indicate how you want to open the URL.
- `completionHandler`: The completion handler block to call asynchronously with the results. AppKit executes the completion handler on a concurrent queue. The handler block has no return value and takes the following parameters:

  - **app**: On success, this parameter contains a reference to the app that opened the URL. If the app didn’t open the URL successfully, this parameter is `nil`.
  - **error**: On failure, this parameter contains an [`NSError`](../../Foundation/nserror.md) object indicating the reason for the failure. If the method opened the URL successfully, this parameter is `nil`.

## See Also

### Opening URLs
- [func open([URL], withApplicationAt: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](./open%28_,withapplicationat,configuration,completionhandler%29.md)
  Opens one or more URLs asynchronously in the specified app using the provided options.
- [func open(URL) -> Bool](./open%28_%29.md)
  Opens the location at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/open(_:configuration:completionhandler:))*