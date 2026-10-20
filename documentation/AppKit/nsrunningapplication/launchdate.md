# launchDate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates the date when the application was launched.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var launchDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * launchDate;
```

#### Discussion

This property is only available for applications that were launched by LaunchServices.

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
- [var isFinishedLaunching: Bool](./isfinishedlaunching.md)
  A Boolean value that determines whether the receiver’s process has finished launching.
- [var processIdentifier: pid_t](./processidentifier.md)
  Indicates the process identifier (pid) of the application.
- [var ownsMenuBar: Bool](./ownsmenubar.md)
  Returns whether the application owns the current menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/launchdate)*