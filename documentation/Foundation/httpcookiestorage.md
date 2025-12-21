# HTTPCookieStorage

**Framework**: Foundation  
**Kind**: class

A container that manages the storage of cookies.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HTTPCookieStorage
```

#### Overview

Each stored cookie is represented by an instance of the [`HTTPCookie`](httpcookie.md) class.

##### Sharing Cookie Storage

The persistent cookie storage returned by [`shared`](httpcookiestorage/shared.md) may be available to app extensions or other apps, subject to the following guidelines:

- iOS — Each app and app extension has a unique data container, meaning  they have separate cookie stores. You can obtain a common cookie storage by using the [`sharedCookieStorage(forGroupContainerIdentifier:)`](httpcookiestorage/sharedcookiestorage(forgroupcontaineridentifier:).md) method.
- macOS (non-sandboxed) — As of macOS 10.11, each app has its own cookie storage. Prior to macOS 10.11, a common cookie store is shared among the user’s apps.
- macOS (sandboxed) — Same as iOS.
- [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView) — `UIWebView` instances within an app inherit the parent app’s shared cookie storage.
- [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) — Each `WKWebView` instance has its own cookie storage. See the [`WKHTTPCookieStore`](https://developer.apple.com/documentation/WebKit/WKHTTPCookieStore) class for more information.

Session cookies (where the cookie object’s [`isSessionOnly`](httpcookie/issessiononly.md) property is [`true`](https://developer.apple.com/documentation/Swift/true)) are local to a single process and are not shared.

> **Note**:  In cases where a cookie storage is shared between processes, changes made to the cookie accept policy affect all currently running apps using the cookie storage.

##### Subclassing Notes

The [`HTTPCookieStorage`](httpcookiestorage.md) class is usable as-is, but you can subclass it. For example, you can override the storage methods like [`storeCookies(_:for:)`](httpcookiestorage/storecookies(_:for:).md), [`getCookiesFor(_:completionHandler:)`](httpcookiestorage/getcookiesfor(_:completionhandler:).md) to screen which cookies are stored, or reimplement the storage mechanism for security or other reasons.

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred by the system to equivalent methods that do not. Therefore, you should override the task-based methods when subclassing, as follows:

- Retrieving cookies — Override [`getCookiesFor(_:completionHandler:)`](httpcookiestorage/getcookiesfor(_:completionhandler:).md), instead of or in addition to [`cookies(for:)`](httpcookiestorage/cookies(for:).md).
- Adding cookies — Override [`storeCookies(_:for:)`](httpcookiestorage/storecookies(_:for:).md), instead of or in addition to [`setCookies(_:for:mainDocumentURL:)`](httpcookiestorage/setcookies(_:for:maindocumenturl:).md).

## Topics

### Getting the shared cookie storage object
- [class var shared: HTTPCookieStorage](httpcookiestorage/shared.md)
  The shared cookie storage instance.
- [class func sharedCookieStorage(forGroupContainerIdentifier: String) -> HTTPCookieStorage](httpcookiestorage/sharedcookiestorage(forgroupcontaineridentifier:).md)
  Returns the cookie storage instance for the container associated with the specified app group identifier.
### Getting and setting the cookie accept policy
- [var cookieAcceptPolicy: HTTPCookie.AcceptPolicy](httpcookiestorage/cookieacceptpolicy.md)
  The cookie storage’s cookie accept policy.
- [HTTPCookie.AcceptPolicy](httpcookie/acceptpolicy.md)
  Cookie acceptance policies implemented by the [`HTTPCookieStorage`](httpcookiestorage.md) class.
### Adding and removing cookies
- [func removeCookies(since: Date)](httpcookiestorage/removecookies(since:).md)
  Removes cookies that were stored after a given date.
- [func deleteCookie(HTTPCookie)](httpcookiestorage/deletecookie(_:).md)
  Deletes the specified cookie from the cookie storage.
- [func setCookie(HTTPCookie)](httpcookiestorage/setcookie(_:).md)
  Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [func setCookies([HTTPCookie], for: URL?, mainDocumentURL: URL?)](httpcookiestorage/setcookies(_:for:maindocumenturl:).md)
  Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [func storeCookies([HTTPCookie], for: URLSessionTask)](httpcookiestorage/storecookies(_:for:).md)
  Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.
### Retrieving cookies
- [var cookies: [HTTPCookie]?](httpcookiestorage/cookies.md)
  The cookie storage’s cookies.
- [func getCookiesFor(URLSessionTask, completionHandler: ([HTTPCookie]?) -> Void)](httpcookiestorage/getcookiesfor(_:completionhandler:).md)
  Fetches cookies relevant to the specified task and passes them to the completion handler.
- [func cookies(for: URL) -> [HTTPCookie]?](httpcookiestorage/cookies(for:).md)
  Returns all the cookie storage’s cookies that are sent to a specified URL.
- [func sortedCookies(using: [NSSortDescriptor]) -> [HTTPCookie]](httpcookiestorage/sortedcookies(using:).md)
  Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.
### Tracking cookie storage changes
- [static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md)
  A notification posted when the cookies stored in the cookie storage have changed.
- [static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged.md)
  A notification posted when the acceptance policy of the cookie storage has changed.
### Structures
- [HTTPCookieStorage.CookiesChangedMessage](httpcookiestorage/cookieschangedmessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HTTPCookie](httpcookie.md)
  A representation of an HTTP cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage)*