# init(identifier:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (NSBundle *) bundleWithIdentifier:(NSString *) identifier;
```

## Return Value

The `NSBundle` object with the bundle identifier `identifier`, or `nil` if the requested bundle is not found on the system. This method creates and returns a new `NSBundle` object if there is no existing bundle associated with `identifier`. Otherwise, the existing instance is returned.

## Discussion

This method is typically used by frameworks and plug-ins to locate their own bundle at runtime. This method may be somewhat more efficient than trying to locate the bundle using the [`init(for:)`](./init%28for%29.md) method. However, if the initial lookup of an already loaded and cached bundle with the specified identifier fails, this method uses potentially time-consuming heuristics to attempt to locate the bundle. As an optimization, you can use the [`bundleWithPath:`](../nsbundle/bundlewithpath_.md) or [`init(url:)`](./init%28url%29-a2t0.md) method instead to avoid file system traversal.

## Parameters

- `identifier`: The identifier for an existing `NSBundle` instance.

## See Also

### Creating and initializing a bundle
- [convenience init?(url: URL)](./init%28url%29-a2t0.md)
  Returns an `NSBundle` object that corresponds to the specified file URL.
- [init(for: AnyClass)](./init%28for%29.md)
  Returns the `NSBundle` object with which the specified class is associated.
- [init?(path: String)](./init%28path%29.md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.
- [+ bundleWithPath:](../nsbundle/bundlewithpath_.md)
  Returns an `NSBundle` object that corresponds to the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/init(identifier:))*