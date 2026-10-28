# bundleIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates the `CFBundleIdentifier` of the application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var bundleIdentifier: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * bundleIdentifier;
```

## Discussion

The value of this property will be `nil` if the application does not have an Info.plist.

## See Also

### Application information
- [var localizedName: String?](./localizedname.md)
  Indicates the localized name of the application.
- [var icon: NSImage?](./icon.md)
  Returns the icon for the receiver’s application.
- [var bundleURL: URL?](./bundleurl.md)
  Indicates the URL to the application’s bundle.
- [var executableArchitecture: Int](./executablearchitecture.md)
  Indicates the executing processor architecture for the application.
- [var executableURL: URL?](./executableurl.md)
  Indicates the URL to the application’s executable.
- [var launchDate: Date?](./launchdate.md)
  Indicates the date when the application was launched.
- [var isFinishedLaunching: Bool](./isfinishedlaunching.md)
  A Boolean value that determines whether the receiver’s process has finished launching.
- [var processIdentifier: pid_t](./processidentifier.md)
  Indicates the process identifier (pid) of the application.
- [var ownsMenuBar: Bool](./ownsmenubar.md)
  Returns whether the application owns the current menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/bundleidentifier)*