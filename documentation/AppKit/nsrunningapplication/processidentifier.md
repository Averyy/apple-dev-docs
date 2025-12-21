# processIdentifier

**Framework**: AppKit  
**Kind**: property

Indicates the process identifier (pid) of the application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var processIdentifier: pid_t { get }
```

#### Discussion

Not all applications have a pid.  Applications without a pid return a value of -1.

Do not rely on this for comparing processes, instead compare NSRunningApplication instances using [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)).

## See Also

- [var localizedName: String?](nsrunningapplication/localizedname.md)
  Indicates the localized name of the application.
- [var icon: NSImage?](nsrunningapplication/icon.md)
  Returns the icon for the receiver’s application.
- [var bundleIdentifier: String?](nsrunningapplication/bundleidentifier.md)
  Indicates the `CFBundleIdentifier` of the application.
- [var bundleURL: URL?](nsrunningapplication/bundleurl.md)
  Indicates the URL to the application’s bundle.
- [var executableArchitecture: Int](nsrunningapplication/executablearchitecture.md)
  Indicates the executing processor architecture for the application.
- [var executableURL: URL?](nsrunningapplication/executableurl.md)
  Indicates the URL to the application’s executable.
- [var launchDate: Date?](nsrunningapplication/launchdate.md)
  Indicates the date when the application was launched.
- [var isFinishedLaunching: Bool](nsrunningapplication/isfinishedlaunching.md)
  A Boolean value that determines whether the receiver’s process has finished launching.
- [var ownsMenuBar: Bool](nsrunningapplication/ownsmenubar.md)
  Returns whether the application owns the current menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/processidentifier)*