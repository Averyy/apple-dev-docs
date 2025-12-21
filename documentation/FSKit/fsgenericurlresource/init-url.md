# init(url:)

**Framework**: FSKit  
**Kind**: init

Creates a generic URL resource with the given URL.

**Availability**:
- macOS 26.0+

## Declaration

```swift
init(url: URL)
```

## Parameters

- `url`: A URL that provides the content of the file system. The format of this URL is completely arbitrary. It’s up to your extension to access the contents represented by the URL and make them available as an   that FSKit can load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgenericurlresource/init(url:))*