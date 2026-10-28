# processIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates the process identifier (pid) of the application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var processIdentifier: pid_t { get }
```

```objc
@property (readonly) pid_t processIdentifier;
```

## Discussion

Not all applications have a pid.  Applications without a pid return a value of -1.

Do not rely on this for comparing processes, instead compare NSRunningApplication instances using [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md).

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
- [var isFinishedLaunching: Bool](./isfinishedlaunching.md)
  A Boolean value that determines whether the receiver’s process has finished launching.
- [var ownsMenuBar: Bool](./ownsmenubar.md)
  Returns whether the application owns the current menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/processidentifier)*