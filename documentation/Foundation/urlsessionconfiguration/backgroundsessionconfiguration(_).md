# backgroundSessionConfiguration(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`background(withIdentifier:)`](./background%28withidentifier%29.md) instead.

## Declaration

```swift
class func backgroundSessionConfiguration(_ identifier: String) -> URLSessionConfiguration
```

```objc
+ (NSURLSessionConfiguration *) backgroundSessionConfiguration:(NSString *) identifier;
```

#### Return Value

A URL session configuration object that causes upload and download tasks to be performed by the system in a separate process.

## Parameters

- `identifier`: The unique identifier for the configuration object. This parameter must not be `nil` or an empty string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/backgroundsessionconfiguration(_:))*