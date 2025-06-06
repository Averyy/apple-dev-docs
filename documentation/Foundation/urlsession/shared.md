# shared

**Framework**: Foundation  
**Kind**: property

The shared singleton session object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var shared: URLSession { get }
```

## Mentions

- [Fetching website data into memory](fetching-website-data-into-memory.md)

#### Discussion

For basic requests, the [`URLSession`](urlsession.md) class provides a shared singleton session object that gives you a reasonable default behavior for creating tasks. Use the shared session to fetch the contents of a URL to memory with just a few lines of code.

Unlike the other session types, you don’t create the shared session; you merely access it by using this property directly. As a result, you don’t provide a delegate or a configuration object.

##### Limitations of the Shared Session

Because the shared session has neither a delegate nor a customizable configuration object, the shared session has important limitations:

- You can’t obtain data incrementally as it arrives from the server.
- You can’t significantly customize the default connection behavior.
- Your ability to perform authentication is limited.
- You can’t perform background downloads or uploads when your app isn’t running.

The shared session uses the shared [`URLCache`](urlcache.md), [`HTTPCookieStorage`](httpcookiestorage.md), and [`URLCredentialStorage`](urlcredentialstorage.md) objects, uses a shared custom networking protocol list (configured with [`registerClass(_:)`](urlprotocol/registerclass(_:).md) and [`unregisterClass(_:)`](urlprotocol/unregisterclass(_:).md)), and is based on a default configuration.

In general, when working with a shared session, you should avoid customizing the cache, cookie storage, or credential storage (unless you are already doing so with [`NSURLConnection`](nsurlconnection.md)). There’s a good chance that you’ll outgrow the capabilities of the default session, at which point you’ll have to rewrite all of those customizations to work with your custom URL sessions.

In other words, if you’re doing  with caches, cookies, authentication, or custom networking protocols, you should probably be using a default session instead of the shared session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/shared)*