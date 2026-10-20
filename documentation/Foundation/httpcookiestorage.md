# HTTPCookieStorage

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSHTTPCookieStorage : NSObject
```

#### Overview

Each stored cookie is represented by an instance of the [`HTTPCookie`](./httpcookie.md) class.

##### Sharing cookie storage

The persistent cookie storage returned by [`shared`](./httpcookiestorage/shared.md) may be available to app extensions or other apps, subject to the following guidelines:

- iOS — Each app and app extension has a unique data container, meaning  they have separate cookie stores. You can obtain a common cookie storage by using the [`sharedCookieStorage(forGroupContainerIdentifier:)`](./httpcookiestorage/sharedcookiestorage%28forgroupcontaineridentifier%29.md) method.
- macOS (non-sandboxed) — As of macOS 10.11, each app has its own cookie storage. Prior to macOS 10.11, a common cookie store is shared among the user’s apps.
- macOS (sandboxed) — Same as iOS.
- [`UIWebView`](../UIKit/uiwebview.md) — `UIWebView` instances within an app inherit the parent app’s shared cookie storage.
- [`WKWebView`](../WebKit/wkwebview.md) — Each `WKWebView` instance has its own cookie storage. See the [`WKHTTPCookieStore`](../WebKit/wkhttpcookiestore.md) class for more information.

Session cookies (where the cookie object’s [`isSessionOnly`](./httpcookie/issessiononly.md) property is [`true`](../Swift/true.md)) are local to a single process and are not shared.

> **Note**:  In cases where a cookie storage is shared between processes, changes made to the cookie accept policy affect all currently running apps using the cookie storage.

##### Subclassing notes

The [`HTTPCookieStorage`](./httpcookiestorage.md) class is usable as-is, but you can subclass it. For example, you can override the storage methods like [`storeCookies(_:for:)`](./httpcookiestorage/storecookies%28_,for%29.md), [`getCookiesFor(_:completionHandler:)`](./httpcookiestorage/getcookiesfor%28_,completionhandler%29.md) to screen which cookies are stored, or reimplement the storage mechanism for security or other reasons.

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred by the system to equivalent methods that do not. Therefore, you should override the task-based methods when subclassing, as follows:

- Retrieving cookies — Override [`getCookiesFor(_:completionHandler:)`](./httpcookiestorage/getcookiesfor%28_,completionhandler%29.md), instead of or in addition to [`cookies(for:)`](./httpcookiestorage/cookies%28for%29.md).
- Adding cookies — Override [`storeCookies(_:for:)`](./httpcookiestorage/storecookies%28_,for%29.md), instead of or in addition to [`setCookies(_:for:mainDocumentURL:)`](./httpcookiestorage/setcookies%28_,for,maindocumenturl%29.md).

## Topics

### Getting the shared cookie storage object
- [class var shared: HTTPCookieStorage](./httpcookiestorage/shared.md)
  The shared cookie storage instance.
- [class func sharedCookieStorage(forGroupContainerIdentifier: String) -> HTTPCookieStorage](./httpcookiestorage/sharedcookiestorage%28forgroupcontaineridentifier%29.md)
  Returns the cookie storage instance for the container associated with the specified app group identifier.
### Getting and setting the cookie accept policy
- [var cookieAcceptPolicy: HTTPCookie.AcceptPolicy](./httpcookiestorage/cookieacceptpolicy.md)
  The cookie storage’s cookie accept policy.
- [HTTPCookie.AcceptPolicy](./httpcookie/acceptpolicy.md)
  Cookie acceptance policies implemented by the [`HTTPCookieStorage`](./httpcookiestorage.md) class.
### Adding and removing cookies
- [func removeCookies(since: Date)](./httpcookiestorage/removecookies%28since%29.md)
  Removes cookies that were stored after a given date.
- [func deleteCookie(HTTPCookie)](./httpcookiestorage/deletecookie%28_%29.md)
  Deletes the specified cookie from the cookie storage.
- [func setCookie(HTTPCookie)](./httpcookiestorage/setcookie%28_%29.md)
  Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [func setCookies([HTTPCookie], for: URL?, mainDocumentURL: URL?)](./httpcookiestorage/setcookies%28_,for,maindocumenturl%29.md)
  Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [func storeCookies([HTTPCookie], for: URLSessionTask)](./httpcookiestorage/storecookies%28_,for%29.md)
  Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.
### Retrieving cookies
- [var cookies: [HTTPCookie]?](./httpcookiestorage/cookies.md)
  The cookie storage’s cookies.
- [func getCookiesFor(URLSessionTask, completionHandler: ([HTTPCookie]?) -> Void)](./httpcookiestorage/getcookiesfor%28_,completionhandler%29.md)
  Fetches cookies relevant to the specified task and passes them to the completion handler.
- [func cookies(for: URL) -> [HTTPCookie]?](./httpcookiestorage/cookies%28for%29.md)
  Returns all the cookie storage’s cookies that are sent to a specified URL.
- [func sortedCookies(using: [NSSortDescriptor]) -> [HTTPCookie]](./httpcookiestorage/sortedcookies%28using%29.md)
  Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.
### Tracking cookie storage changes
- [static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name](./nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md)
  A notification posted when the cookies stored in the cookie storage have changed.
- [HTTPCookieStorage.CookiesChangedMessage](./httpcookiestorage/cookieschangedmessage.md)
  A message a cookie storage instance sends when its cookies change.
- [static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name](./nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged.md)
  A notification posted when the acceptance policy of the cookie storage has changed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Cookies
- [class HTTPCookie](./httpcookie.md)
  A representation of an HTTP cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage)*