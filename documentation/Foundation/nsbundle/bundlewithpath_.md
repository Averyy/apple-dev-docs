# bundleWithPath:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSBundle` object that corresponds to the specified directory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) bundleWithPath:(NSString *) path;
```

#### Return Value

The `NSBundle` object that corresponds to `path`, or `nil` if `path` does not identify an accessible bundle directory.

#### Discussion

This method allocates and initializes the returned object if there is no existing `NSBundle` associated with `path`, in which case it returns the existing object.

## Parameters

- `path`: The path to a directory. This must be a full pathname for a directory; if it contains any symbolic links, they must be resolvable.

## See Also

### Related Documentation
- [class var main: Bundle](../bundle/main.md)
  Returns the bundle object that contains the current executable.
### Creating and initializing a bundle
- [convenience init?(url: URL)](../bundle/init%28url%29-a2t0.md)
  Returns an `NSBundle` object that corresponds to the specified file URL.
- [init(for: AnyClass)](../bundle/init%28for%29.md)
  Returns the `NSBundle` object with which the specified class is associated.
- [init?(identifier: String)](../bundle/init%28identifier%29.md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [init?(path: String)](../bundle/init%28path%29.md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundle/bundlewithpath:)*