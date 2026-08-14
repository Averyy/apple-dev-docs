# isDiscretionary

**Framework**: Foundation  
**Kind**: property

A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isDiscretionary: Bool { get set }
```

## Mentions

- [Downloading files in the background](downloading-files-in-the-background.md)

#### Discussion

For configuration objects created using the [`background(withIdentifier:)`](urlsessionconfiguration/background(withidentifier:).md) method, use this property to give the system control over when transfers should occur. This property is ignored for configuration objects created using other methods.

When transferring large amounts of data, you are encouraged to set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true). Doing so lets the system schedule those transfers at times that are more optimal for the device. For example, the system might delay transferring large files until the device is plugged in and connected to the network via Wi-Fi. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

The session object applies the value of this property only to transfers that your app starts while it is in the foreground. For transfers started while your app is in the background, the system always starts transfers at its discretion—in other words, the system assumes this property is [`true`](https://developer.apple.com/documentation/swift/true) and ignores any value you specified.

## See Also

- [var sessionSendsLaunchEvents: Bool](urlsessionconfiguration/sessionsendslaunchevents.md)
  A Boolean value that indicates whether the app should be resumed or launched in the background when transfers finish.
- [var shouldUseExtendedBackgroundIdleMode: Bool](urlsessionconfiguration/shoulduseextendedbackgroundidlemode.md)
  A Boolean value that indicates whether TCP connections should be kept open when the app moves to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/isdiscretionary)*