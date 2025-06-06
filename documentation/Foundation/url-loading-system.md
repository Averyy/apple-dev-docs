# URL Loading System

**Framework**: Foundation

Interact with URLs and communicate with servers using standard Internet protocols.

#### Overview

The URL Loading System provides access to resources identified by URLs, using standard protocols like `https` or custom protocols you create. Loading is performed asynchronously, so your app can remain responsive and handle incoming data or errors as they arrive.

You use a [`URLSession`](urlsession.md) instance to create one or more [`URLSessionTask`](urlsessiontask.md) instances, which can fetch and return data to your app, download files, or upload data and files to remote locations. To configure a session, you use a [`URLSessionConfiguration`](urlsessionconfiguration.md) object, which controls behavior like how to use caches and cookies, or whether to allow connections on a cellular network.

You can use one session repeatedly to create tasks. For example, a web browser might have separate sessions for regular and private browsing use, where the private session doesn’t cache its data. [`Figure 1`](url_loading_system#2927983.md) shows how two sessions with these configurations can then create multiple tasks.

![Figure showing two scenarios, default browsing and private browsing, each with a URL Session creating multiple URL Session Tasks. In the default browsing case, the URL Session contains a default configuration. In the private browsing case, it contains an ephemeral configuration.](https://docs-assets.developer.apple.com/published/cbc45a3ebfd73610ee2e1296aa49f88e/media-2927983%402x.png)

Each session is associated with a delegate to receive periodic updates (or errors). The default delegate calls a completion handler block that you provide; if you choose to provide your own custom delegate, this block is not called.

You can configure a session to run in the background, so that while the app is suspended, the system can download data on its behalf and wake up the app to deliver the results.

## Topics

### Essentials
- [Fetching website data into memory](fetching-website-data-into-memory.md)
  Receive data directly into memory by creating a data task from a URL session.
- [Analyzing HTTP traffic with Instruments](analyzing-http-traffic-with-instruments.md)
  Measure HTTP-based network performance and usage of your apps.
- [class URLSession](urlsession.md)
  An object that coordinates a group of related, network data transfer tasks.
- [class URLSessionTask](urlsessiontask.md)
  A task, like downloading a specific resource, performed in a URL session.
### Requests and responses
- [struct URLRequest](urlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSURLRequest](nsurlrequest.md)
  A URL load request that is independent of protocol or URL scheme.
- [class NSMutableURLRequest](nsmutableurlrequest.md)
  A mutable URL load request that is independent of protocol or URL scheme.
- [class URLResponse](urlresponse.md)
  The metadata associated with the response to a URL load request, independent of protocol and URL scheme.
- [class HTTPURLResponse](httpurlresponse.md)
  The metadata associated with the response to an HTTP protocol URL load request.
### Uploading
- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md)
  Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [Uploading data to a website](uploading-data-to-a-website.md)
  Post data from your app to servers.
- [Uploading streams of data](uploading-streams-of-data.md)
  Send a stream of data to a server.
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)
  Pause and resume an upload without starting over, even when the connection is interrupted.
### Downloading
- [Downloading files from websites](downloading-files-from-websites.md)
  Download files directly to the filesystem.
- [Pausing and resuming downloads](pausing-and-resuming-downloads.md)
  Allow the user to resume a download without starting over.
- [Downloading files in the background](downloading-files-in-the-background.md)
  Create tasks that download files while your app is inactive.
### Cache behavior
- [Accessing cached data](accessing-cached-data.md)
  Control how URL requests make use of previously cached data.
- [class CachedURLResponse](cachedurlresponse.md)
  A cached response to a URL request.
- [class URLCache](urlcache.md)
  An object that maps URL requests to cached response objects.
### Authentication and credentials
- [Handling an authentication challenge](handling-an-authentication-challenge.md)
  Respond appropriately when a server demands authentication for a URL request.
- [class URLAuthenticationChallenge](urlauthenticationchallenge.md)
  A challenge from a server requiring authentication from the client.
- [class URLCredential](urlcredential.md)
  `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [class URLCredentialStorage](urlcredentialstorage.md)
  The manager of a shared credentials cache.
- [class URLProtectionSpace](urlprotectionspace.md)
  A server or an area on a server, commonly referred to as a realm, that requires authentication.
### Network activity attribution
- [Inspecting app activity data](../Network/inspecting-app-activity-data.md)
  Verify that your app accesses only the user data and network resources that you expect it to access.
- [Indicating the source of network activity](../Network/indicating-the-source-of-network-activity.md)
  Control whether the App Privacy Report attributes network traffic to the app or to the user.
### Cookies
- [class HTTPCookie](httpcookie.md)
  A representation of an HTTP cookie.
- [class HTTPCookieStorage](httpcookiestorage.md)
  A container that manages the storage of cookies.
### Errors
- [struct URLError](urlerror.md)
  Error codes returned by URL loading APIs.
- [URL Loading System error info keys](url-loading-system-error-info-keys.md)
  Recognize these keys from the user info dictionary of error objects produced by URL Loading APIs.
### Legacy
- [Legacy URL Loading Systems](legacy-url-loading-systems.md)
  Migrate your code away from using these legacy objects.

## See Also

- [Bonjour](bonjour.md)
  Advertise services for easy discovery on local networks, or discover services advertised by others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url-loading-system)*