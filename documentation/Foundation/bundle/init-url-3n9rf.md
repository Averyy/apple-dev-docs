# init(url:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSBundle` object initialized to correspond to the specified file URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(url: URL)
```

#### Return Value

An `NSBundle` object initialized to correspond to @c url, or @c nil if @c url doesn’t exist or the user doesn’t have access to it.

#### Discussion

This method initializes and returns a new instance only if there is no existing bundle associated with @c url, otherwise it deallocates @c self and returns the existing object.

## Parameters

- `url`: The file URL to a directory. This must be a full URL for a directory; if it contains any symbolic links, they must be resolvable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(url:)-3n9rf)*