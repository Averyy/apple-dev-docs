# setUpConnection(for:options:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Prewarms a network connection to the specified host without creating an asset.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
class func setUpConnection(for url: URL, options: [String : Any]? = nil, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func setUpConnection(for url: URL, options: [String : Any]? = nil) async throws
```

```objc
+ (void) setUpConnectionForURL:(NSURL *) url options:(NSDictionary<NSString *,id> *) options completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

The connection will be established using the same URLSession configuration that would be used for AVURLAsset instances created with the specified options. This allows the connection to be reused when an actual asset is later created. This is a best-effort API.

## Parameters

- `url`: URL containing the scheme, hostname and port for which to establish the connection. This should mirror the eventual asset URL. The actual HTTP request will not be sent (i.e. URL path is ignored).
- `options`: The same AVURLAsset creation options dictionary that will be used when creating the eventual AVURLAsset instance.
- `completionHandler`: An optional completion handler called when the prewarming attempt completes. The handler receives an NSError if the prewarming failed, or nil on success. The completion handler will always be invoked asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/setupconnection(for:options:completionhandler:))*