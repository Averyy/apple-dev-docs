# init(path:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithPath:(NSString *) path;
```

## Return Value

An `NSBundle` object initialized to correspond to `fullPath`. This method initializes and returns a new instance only if there is no existing bundle associated with `fullPath`, otherwise it deallocates `self` and returns the existing object. If `fullPath` doesn’t exist or the user doesn’t have access to it, returns `nil`.

## Discussion

It’s not necessary to allocate and initialize an instance for the main bundle; use the [`main`](./main.md) class method to get this instance. You can also use the [`bundleWithPath:`](../nsbundle/bundlewithpath_.md) class method to obtain a bundle identified by its directory path.

## Parameters

- `path`: The path to a directory. This must be a full pathname for a directory; if it contains any symbolic links, they must be resolvable.

## See Also

### Creating and initializing a bundle
- [convenience init?(url: URL)](./init%28url%29-a2t0.md)
  Returns an `NSBundle` object that corresponds to the specified file URL.
- [init(for: AnyClass)](./init%28for%29.md)
  Returns the `NSBundle` object with which the specified class is associated.
- [init?(identifier: String)](./init%28identifier%29.md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [+ bundleWithPath:](../nsbundle/bundlewithpath_.md)
  Returns an `NSBundle` object that corresponds to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(path:))*