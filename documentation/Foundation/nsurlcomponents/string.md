# string

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A URL derived from the components object, in string form.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var string: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * string;
```

#### Discussion

If the receiver has an authority component (user, password, host, or port) and a path component, then the path must either begin with `"/"` or be an empty string. Otherwise, this property contains `nil`.

If the receiver  *does not* have an authority component (user, password, host, or port) and has a path component, the path component must not start with `"//"`. If it does, this property contains `nil`.

This property can be used only to obtain a URL string based on the values of the other properties. To configure a components object based on an existing URL string, call either the [`componentsWithString:`](./componentswithstring_.md) or [`init(string:)`](./init%28string%29.md) method.

## See Also

### Getting the URL
- [var url: URL?](./url.md)
  A URL object derived from the components object.
- [func url(relativeTo: URL?) -> URL?](./url%28relativeto%29.md)
  Returns a URL object derived from the components object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/string)*