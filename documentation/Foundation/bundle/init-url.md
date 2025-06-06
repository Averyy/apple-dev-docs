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
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(url: URL)
```

#### Return Value

An `NSBundle` object initialized to correspond to `url`. This method initializes and returns a new instance only if there is no existing bundle associated with `url`, otherwise it deallocates `self` and returns the existing object. If `url` doesn’t exist or the user doesn’t have access to it, returns `nil`.

#### Discussion

It’s not necessary to allocate and initialize an instance for the main bundle; use the [`main`](bundle/main.md) class method to get this instance. You can also use the [`bundleWithURL:`](nsbundle/bundlewithurl:.md) class method to obtain a bundle identified by its file URL.

## Parameters

- `url`: The file URL to a directory. This must be a full URL for a directory; if it contains any symbolic links, they must be resolvable.

## See Also

- [init(for: AnyClass)](bundle/init(for:).md)
  Returns the `NSBundle` object with which the specified class is associated.
- [init?(identifier: String)](bundle/init(identifier:).md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [init?(path: String)](bundle/init(path:).md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(url:))*