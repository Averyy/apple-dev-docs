# init(identifier:)

**Framework**: Foundation  
**Kind**: init

Returns the `NSBundle` instance that has the specified bundle identifier.

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
init?(identifier: String)
```

#### Return Value

The `NSBundle` object with the bundle identifier `identifier`, or `nil` if the requested bundle is not found on the system. This method creates and returns a new `NSBundle` object if there is no existing bundle associated with `identifier`. Otherwise, the existing instance is returned.

#### Discussion

This method is typically used by frameworks and plug-ins to locate their own bundle at runtime. This method may be somewhat more efficient than trying to locate the bundle using the [`init(for:)`](bundle/init(for:).md) method. However, if the initial lookup of an already loaded and cached bundle with the specified identifier fails, this method uses potentially time-consuming heuristics to attempt to locate the bundle. As an optimization, you can use the [`bundleWithPath:`](nsbundle/bundlewithpath:.md) or [`bundleWithURL:`](nsbundle/bundlewithurl:.md) method instead to avoid file system traversal.

## Parameters

- `identifier`: The identifier for an existing   instance.

## See Also

- [init(for: AnyClass)](bundle/init(for:).md)
  Returns the `NSBundle` object with which the specified class is associated.
- [convenience init?(url: URL)](bundle/init(url:).md)
  Returns an `NSBundle` object initialized to correspond to the specified file URL.
- [init?(path: String)](bundle/init(path:).md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(identifier:))*