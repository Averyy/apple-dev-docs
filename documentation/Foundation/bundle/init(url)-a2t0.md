# init(url:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSBundle` object that corresponds to the specified file URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(url: URL)
```

```objc
+ (instancetype) bundleWithURL:(NSURL *) url;
```

#### Return Value

The `NSBundle` object that corresponds to `url`, or `nil` if `url` does not identify an accessible bundle directory.

#### Discussion

This method allocates and initializes the returned object if there is no existing `NSBundle` associated with `url`, in which case it returns the existing object.

## Parameters

- `url`: The URL to a directory. This must be a URL for a directory; if it contains any symbolic links, they must be resolvable.

## See Also

### Creating and initializing a bundle
- [init(for: AnyClass)](./init%28for%29.md)
  Returns the `NSBundle` object with which the specified class is associated.
- [init?(identifier: String)](./init%28identifier%29.md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [init?(path: String)](./init%28path%29.md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(url:)-a2t0)*