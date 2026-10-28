# isFinishedLaunching

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the receiver’s process has finished launching.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isFinishedLaunching: Bool { get }
```

```objc
@property (readonly, getter=isFinishedLaunching) BOOL finishedLaunching;
```

## Discussion

The value of this property corresponds to the running application having received an [`didFinishLaunchingNotification`](../nsapplication/didfinishlaunchingnotification.md) notification internally. Some applications do not post this notification (applications that do not rely on [`NSApplication`](../nsapplication.md)) and so are never reported as finished launching.

This property is observable using key-value observing.

## See Also

### Application information
- [var localizedName: String?](./localizedname.md)
  Indicates the localized name of the application.
- [var icon: NSImage?](./icon.md)
  Returns the icon for the receiver’s application.
- [var bundleIdentifier: String?](./bundleidentifier.md)
  Indicates the `CFBundleIdentifier` of the application.
- [var bundleURL: URL?](./bundleurl.md)
  Indicates the URL to the application’s bundle.
- [var executableArchitecture: Int](./executablearchitecture.md)
  Indicates the executing processor architecture for the application.
- [var executableURL: URL?](./executableurl.md)
  Indicates the URL to the application’s executable.
- [var launchDate: Date?](./launchdate.md)
  Indicates the date when the application was launched.
- [var processIdentifier: pid_t](./processidentifier.md)
  Indicates the process identifier (pid) of the application.
- [var ownsMenuBar: Bool](./ownsmenubar.md)
  Returns whether the application owns the current menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/isfinishedlaunching)*