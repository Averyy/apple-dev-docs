# error

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The error that prevented the content from being downloaded.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSError * error;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

#### Discussion

The value of this property is valid only when the [`downloadState`](./downloadstate.md) property is set to [`SKDownloadState.failed`](../skdownloadstate/failed.md).

## See Also

### Accessing a Completed Download
- [var contentURL: URL?](./contenturl.md)
  The local location of the downloaded file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/error)*