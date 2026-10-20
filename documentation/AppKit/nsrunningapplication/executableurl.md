# executableURL

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates the URL to the application’s executable.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var executableURL: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * executableURL;
```

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
- [var launchDate: Date?](./launchdate.md)
  Indicates the date when the application was launched.
- [var isFinishedLaunching: Bool](./isfinishedlaunching.md)
  A Boolean value that determines whether the receiver’s process has finished launching.
- [var processIdentifier: pid_t](./processidentifier.md)
  Indicates the process identifier (pid) of the application.
- [var ownsMenuBar: Bool](./ownsmenubar.md)
  Returns whether the application owns the current menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/executableurl)*