# sharedCookieStorage(forGroupContainerIdentifier:)

**Framework**: Foundation  
**Kind**: method

Returns the cookie storage instance for the container associated with the specified app group identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func sharedCookieStorage(forGroupContainerIdentifier identifier: String) -> HTTPCookieStorage
```

#### Discussion

By default, apps and associated app extensions will have different data containers. As a result, the value of the [`HTTPCookieStorage`](httpcookiestorage.md) class’s [`shared`](httpcookiestorage/shared.md) property will refer to different persistent cookie stores when called by the app and by its extensions.You can use this method to create a persistent cookie storage available to all apps and extensions with access to the same app group.

Subsequent calls to the this method with the same identifier will return the same storage instance.

## Parameters

- `identifier`: The app group identifier.

## See Also

- [class var shared: HTTPCookieStorage](httpcookiestorage/shared.md)
  The shared cookie storage instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/sharedcookiestorage(forgroupcontaineridentifier:))*