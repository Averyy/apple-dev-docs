# background(withIdentifier:)

**Framework**: Foundation  
**Kind**: method

Creates a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func background(withIdentifier identifier: String) -> URLSessionConfiguration
```

## Mentions

- [Downloading files in the background](downloading-files-in-the-background.md)

#### Return Value

A configuration object that causes the system to perform upload and download tasks in a separate process.

#### Discussion

Use this method to initialize a configuration object suitable for transferring data files while the app runs in the background. A session configured with this object hands control of the transfers over to the system, which handles the transfers in a separate process. In iOS, this configuration makes it possible for transfers to continue even when the app itself is suspended or terminated.

If an iOS app is terminated by the system and relaunched, the app can use the same `identifier` to create a new configuration object and session and to retrieve the status of transfers that were in progress at the time of termination. This behavior applies only for normal termination of the app by the system. If the user terminates the app from the multitasking screen, the system cancels all of the session’s background transfers. In addition, the system does not automatically relaunch apps that were force quit by the user. The user must explicitly relaunch the app before transfers can begin again.

You can configure an background session to schedule transfers at the discretion of the system for optimal performance using the [`isDiscretionary`](urlsessionconfiguration/isdiscretionary.md) property. When transferring large amounts of data, you are encouraged to set the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true). For an example of using the background configuration, see [`Downloading files in the background`](downloading-files-in-the-background.md).

## Parameters

- `identifier`: The unique identifier for the configuration object. This parameter must not be   or an empty string.

## See Also

- [class var `default`: URLSessionConfiguration](urlsessionconfiguration/default.md)
  A default session configuration object.
- [class var ephemeral: URLSessionConfiguration](urlsessionconfiguration/ephemeral.md)
  A session configuration that uses no persistent storage for caches, cookies, or credentials.
- [init()](urlsessionconfiguration/init.md)
  Creates an empty session configuration.
- [class func new() -> Self](urlsessionconfiguration/new.md)
  Creates an empty session configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/background(withidentifier:))*