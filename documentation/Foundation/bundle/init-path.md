# init(path:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSBundle` object initialized to correspond to the specified directory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(path: String)
```

#### Return Value

An `NSBundle` object initialized to correspond to `fullPath`. This method initializes and returns a new instance only if there is no existing bundle associated with `fullPath`, otherwise it deallocates `self` and returns the existing object. If `fullPath` doesn’t exist or the user doesn’t have access to it, returns `nil`.

#### Discussion

It’s not necessary to allocate and initialize an instance for the main bundle; use the [`main`](bundle/main.md) class method to get this instance. You can also use the [`bundleWithPath:`](nsbundle/bundlewithpath:.md) class method to obtain a bundle identified by its directory path.

## Parameters

- `path`: The path to a directory. This must be a full pathname for a directory; if it contains any symbolic links, they must be resolvable.

## See Also

- [init(for: AnyClass)](bundle/init(for:).md)
  Returns the `NSBundle` object with which the specified class is associated.
- [init?(identifier: String)](bundle/init(identifier:).md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [convenience init?(url: URL)](bundle/init(url:).md)
  Returns an `NSBundle` object initialized to correspond to the specified file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(path:))*