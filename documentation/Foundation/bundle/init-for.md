# init(for:)

**Framework**: Foundation  
**Kind**: init

Returns the `NSBundle` object with which the specified class is associated.

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
init(for aClass: AnyClass)
```

#### Return Value

The `NSBundle` object that dynamically loaded `aClass` (a loadable bundle), the `NSBundle` object for the framework in which `aClass` is defined, or the main bundle object if `aClass` was not dynamically loaded or is not defined in a framework. This method creates and returns a new `NSBundle` object if there is no existing bundle associated with `aClass`. Otherwise, the existing instance is returned.

## Parameters

- `aClass`: A class.

## See Also

- [class var main: Bundle](bundle/main.md)
  Returns the bundle object that contains the current executable.
- [init?(identifier: String)](bundle/init(identifier:).md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [convenience init?(url: URL)](bundle/init(url:).md)
  Returns an `NSBundle` object initialized to correspond to the specified file URL.
- [init?(path: String)](bundle/init(path:).md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(for:))*