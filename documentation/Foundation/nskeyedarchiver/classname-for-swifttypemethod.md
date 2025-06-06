# className(for:)

**Framework**: Foundation  
**Kind**: method

Returns the class name with which the archiver class encodes instances of a given class.

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
class func className(for cls: AnyClass) -> String?
```

#### Return Value

The class name with which [`NSKeyedArchiver`](nskeyedarchiver.md) encodes instances of `cls`. Returns `nil` if [`NSKeyedArchiver`](nskeyedarchiver.md) does not have a translation mapping for `cls`.

## Parameters

- `cls`: The class for which to determine the translation mapping.

## See Also

- [class func setClassName(String?, for: AnyClass)](nskeyedarchiver/setclassname(_:for:)-swift.type.method.md)
  Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [func setClassName(String?, for: AnyClass)](nskeyedarchiver/setclassname(_:for:)-swift.method.md)
  Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.
- [func className(for: AnyClass) -> String?](nskeyedarchiver/classname(for:)-swift.method.md)
  Returns the class name with which this archiver encodes instances of a given class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/classname(for:)-swift.type.method)*