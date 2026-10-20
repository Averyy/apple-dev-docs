# shared

**Framework**: Background Assets  
**Kind**: property  
**Role**: Type Property

The download manager that both the app and the extension share.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class var shared: BADownloadManager { get }
```

```objc
@property (class, strong, readonly) BADownloadManager * sharedManager;
```

#### Discussion

Because the download manager is a shared resource, use the `BADownloadManager/withExclusiveControl(_:)` or [`withExclusiveControl(beforeDate:perform:)`](./withexclusivecontrol%28beforedate,perform%29.md) methods to acquire exclusive control of the manager before you use it to access, schedule, or cancel downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/shared)*