# class(forClassName:)

**Framework**: Foundation  
**Kind**: method

Returns the class from which this unarchiver instantiates an encoded object with a given class name.

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
func `class`(forClassName codedName: String) -> AnyClass?
```

#### Return Value

The class from which the receiver instantiates an encoded object with the class name `codedName`. Returns `nil` if the receiver does not have a translation mapping for `codedName`.

#### Discussion

The class’s separate translation map is not searched.

## Parameters

- `codedName`: The name of a class.

## See Also

- [class func setClass(AnyClass?, forClassName: String)](nskeyedunarchiver/setclass(_:forclassname:)-swift.type.method.md)
  Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.
- [class func `class`(forClassName: String) -> AnyClass?](nskeyedunarchiver/class(forclassname:)-swift.type.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.
- [func setClass(AnyClass?, forClassName: String)](nskeyedunarchiver/setclass(_:forclassname:)-swift.method.md)
  Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/class(forclassname:)-swift.method)*