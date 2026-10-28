# className(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the class name with which this archiver encodes instances of a given class.

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
func className(for cls: AnyClass) -> String?
```

```objc
- (NSString *) classNameForClass:(Class) cls;
```

## Return Value

The class name with which the receiver encodes instances of `cls`. Returns `nil` if the receiver does not have a translation mapping for `cls`. The class’s separate translation map is not searched.

## Parameters

- `cls`: The class for which to determine the translation mapping.

## See Also

### Managing Classes and Class Names
- [class func setClassName(String?, for: AnyClass)](./setclassname%28_,for%29-swift.type.method.md)
  Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [class func className(for: AnyClass) -> String?](./classname%28for%29-swift.type.method.md)
  Returns the class name with which the archiver class encodes instances of a given class.
- [func setClassName(String?, for: AnyClass)](./setclassname%28_,for%29-swift.method.md)
  Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/classname(for:)-swift.method)*