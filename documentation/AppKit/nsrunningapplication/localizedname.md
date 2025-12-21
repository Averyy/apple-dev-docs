# localizedName

**Framework**: AppKit  
**Kind**: property

Indicates the localized name of the application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var localizedName: String? { get }
```

#### Discussion

The value of this property is dependent on the current localization of the application and is suitable for presentation to the user.

## See Also

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
- [var processIdentifier: pid_t](nsrunningapplication/processidentifier.md)
  Indicates the process identifier (pid) of the application.
- [var ownsMenuBar: Bool](nsrunningapplication/ownsmenubar.md)
  Returns whether the application owns the current menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/localizedname)*