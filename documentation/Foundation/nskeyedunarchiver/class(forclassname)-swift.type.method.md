# class(forClassName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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
class func `class`(forClassName codedName: String) -> AnyClass?
```

```objc
+ (Class) classForClassName:(NSString *) codedName;
```

#### Return Value

The class from which `NSKeyedUnarchiver` instantiates an object encoded with the class name `codedName`. Returns `nil` if `NSKeyedUnarchiver` does not have a translation mapping for `codedName`.

## Parameters

- `codedName`: The ostensible name of a class in an archive.

## See Also

### Managing Class Names
- [class func setClass(AnyClass?, forClassName: String)](./setclass%28_,forclassname%29-swift.type.method.md)
  Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.
- [func setClass(AnyClass?, forClassName: String)](./setclass%28_,forclassname%29-swift.method.md)
  Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.
- [func `class`(forClassName: String) -> AnyClass?](./class%28forclassname%29-swift.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/class(forclassname:)-swift.type.method)*