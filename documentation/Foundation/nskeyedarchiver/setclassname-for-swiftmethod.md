# setClassName(_:for:)

**Framework**: Foundation  
**Kind**: method

Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.

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
func setClassName(_ codedName: String?, for cls: AnyClass)
```

#### Discussion

When encoding, the receiver’s translation map overrides any translation that may also be present in the class’s map.

## Parameters

- `codedName`: The name of the class that the receiver uses uses in place of  .
- `cls`: The class for which to set up a translation mapping.

## See Also

- [class func setClassName(String?, for: AnyClass)](nskeyedarchiver/setclassname(_:for:)-swift.type.method.md)
  Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [class func className(for: AnyClass) -> String?](nskeyedarchiver/classname(for:)-swift.type.method.md)
  Returns the class name with which the archiver class encodes instances of a given class.
- [func className(for: AnyClass) -> String?](nskeyedarchiver/classname(for:)-swift.method.md)
  Returns the class name with which this archiver encodes instances of a given class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/setclassname(_:for:)-swift.method)*