# init(for:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (NSBundle *) bundleForClass:(Class) aClass;
```

#### Return Value

The `NSBundle` object that dynamically loaded `aClass` (a loadable bundle), the `NSBundle` object for the framework in which `aClass` is defined, or the main bundle object if `aClass` was not dynamically loaded or is not defined in a framework. This method creates and returns a new `NSBundle` object if there is no existing bundle associated with `aClass`. Otherwise, the existing instance is returned.

## Parameters

- `aClass`: A class.

## See Also

### Related Documentation
- [class var main: Bundle](./main.md)
  Returns the bundle object that contains the current executable.
### Creating and initializing a bundle
- [convenience init?(url: URL)](./init%28url%29-a2t0.md)
  Returns an `NSBundle` object that corresponds to the specified file URL.
- [init?(identifier: String)](./init%28identifier%29.md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [init?(path: String)](./init%28path%29.md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(for:))*