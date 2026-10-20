# hideOtherApplications()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Hides all applications other than the sender.

**Availability**:
- macOS

## Declaration

```swift
func hideOtherApplications()
```

```objc
- (void) hideOtherApplications;
```

#### Discussion

In order to hide all apps except the current one, the user can Command-Option-click an app’s Dock icon.

You must call this method from your app’s main thread.

## See Also

### Launching and Hiding Apps
- [func openApplication(at: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](./openapplication%28at,configuration,completionhandler%29.md)
  Launches the app at the specified URL and asynchronously reports back on the app’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/hideotherapplications())*