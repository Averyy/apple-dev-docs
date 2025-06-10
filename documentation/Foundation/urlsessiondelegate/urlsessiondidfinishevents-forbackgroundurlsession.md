# urlSessionDidFinishEvents(forBackgroundURLSession:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that all messages enqueued for a session have been delivered.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSessionDidFinishEvents(forBackgroundURLSession session: URLSession)
```

## Mentions

- [Downloading files in the background](downloading-files-in-the-background.md)

#### Discussion

In iOS, when a background transfer completes or requires credentials, if your app is no longer running, your app is automatically relaunched in the background, and the app’s `UIApplicationDelegate` is sent an [`application(_:handleEventsForBackgroundURLSession:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:handleEventsForBackgroundURLSession:completionHandler:)) message. This call contains the identifier of the session that caused your app to be launched. You should then store that completion handler before creating a background configuration object with the same identifier, and creating a session with that configuration. The newly created session is automatically reassociated with ongoing background activity.

When your app later receives a [`urlSessionDidFinishEvents(forBackgroundURLSession:)`](urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession:).md) message, this indicates that all messages previously enqueued for this session have been delivered, and that it is now safe to invoke the previously stored completion handler or to begin any internal updates that may result in invoking the completion handler.

> ❗ **Important**:  Because the provided completion handler is part of UIKit, you must call it on your main thread.

## Parameters

- `session`: The session that no longer has any outstanding requests.

## See Also

- [func urlSession(URLSession, didBecomeInvalidWithError: (any Error)?)](urlsessiondelegate/urlsession(_:didbecomeinvalidwitherror:).md)
  Tells the URL session that the session has been invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession:))*