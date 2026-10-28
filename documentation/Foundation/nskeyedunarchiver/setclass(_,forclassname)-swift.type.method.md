# setClass(_:forClassName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.

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
class func setClass(_ cls: AnyClass?, forClassName codedName: String)
```

```objc
+ (void) setClass:(Class) cls forClassName:(NSString *) codedName;
```

## Discussion

When decoding, the class’s translation mapping is used only if no translation is found first in an instance’s separate translation map.

## Parameters

- `cls`: The class with which to replace instances of the class named `codedName`.
- `codedName`: The ostensible name of a class in an archive.

## See Also

### Managing Class Names
- [class func `class`(forClassName: String) -> AnyClass?](./class%28forclassname%29-swift.type.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.
- [func setClass(AnyClass?, forClassName: String)](./setclass%28_,forclassname%29-swift.method.md)
  Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.
- [func `class`(forClassName: String) -> AnyClass?](./class%28forclassname%29-swift.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/setclass(_:forclassname:)-swift.type.method)*