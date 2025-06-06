# setClass(_:forClassName:)

**Framework**: Foundation  
**Kind**: method

Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.

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
func setClass(_ cls: AnyClass?, forClassName codedName: String)
```

#### Discussion

When decoding, the receiver’s translation map overrides any translation that may also be present in the class’s map (see [`setClass(_:forClassName:)`](nskeyedunarchiver/setclass(_:forclassname:)-swift.type.method.md)).

## Parameters

- `cls`: The class with which to replace instances of the class named  .
- `codedName`: The ostensible name of a class in an archive.

## See Also

- [class func setClass(AnyClass?, forClassName: String)](nskeyedunarchiver/setclass(_:forclassname:)-swift.type.method.md)
  Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.
- [class func `class`(forClassName: String) -> AnyClass?](nskeyedunarchiver/class(forclassname:)-swift.type.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.
- [func `class`(forClassName: String) -> AnyClass?](nskeyedunarchiver/class(forclassname:)-swift.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/setclass(_:forclassname:)-swift.method)*