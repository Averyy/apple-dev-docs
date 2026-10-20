# shared

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The shared cookie storage instance.

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
class var shared: HTTPCookieStorage { get }
```

```objc
@property (class, strong, readonly) NSHTTPCookieStorage * sharedHTTPCookieStorage;
```

## See Also

### Getting the shared cookie storage object
- [class func sharedCookieStorage(forGroupContainerIdentifier: String) -> HTTPCookieStorage](./sharedcookiestorage%28forgroupcontaineridentifier%29.md)
  Returns the cookie storage instance for the container associated with the specified app group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/shared)*