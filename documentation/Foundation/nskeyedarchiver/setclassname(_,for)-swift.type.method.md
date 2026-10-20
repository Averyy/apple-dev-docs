# setClassName(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.

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
class func setClassName(_ codedName: String?, for cls: AnyClass)
```

```objc
+ (void) setClassName:(NSString *) codedName forClass:(Class) cls;
```

#### Discussion

When encoding, an archiver consults its own translation map before using the class’ translation map.

## Parameters

- `codedName`: The name of the class that `NSKeyedArchiver` uses in place of `cls`.
- `cls`: The class for which to set up a translation mapping.

## See Also

### Managing Classes and Class Names
- [class func className(for: AnyClass) -> String?](./classname%28for%29-swift.type.method.md)
  Returns the class name with which the archiver class encodes instances of a given class.
- [func setClassName(String?, for: AnyClass)](./setclassname%28_,for%29-swift.method.md)
  Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.
- [func className(for: AnyClass) -> String?](./classname%28for%29-swift.method.md)
  Returns the class name with which this archiver encodes instances of a given class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/setclassname(_:for:)-swift.type.method)*