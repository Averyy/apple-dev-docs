# encodeConditionalObject(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Conditionally archives a given object.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
func encodeConditionalObject(_ object: Any?)
```

```objc
- (void) encodeConditionalObject:(id) object;
```

## Discussion

This method overrides the superclass implementation to allow `object` to be encoded only if it is also encoded unconditionally by another object in the object graph. Conditional encoding lets you encode one part of a graph detached from the rest. (See [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) for more information.)

This method should be invoked only from within an [`encode(with:)`](../nscoding/encode%28with%29.md) method. If `object` is `nil`, the `NSArchiver` object encodes it unconditionally as `nil`. This method raises an `NSInvalidArgumentException` if no root object has been encoded.

## Parameters

- `object`: The object to archive.

## See Also

### Archiving data
- [class func archivedData(withRootObject: Any) -> Data](./archiveddata%28withrootobject%29.md)
  Returns a data object containing the encoded form of the object graph whose root object is given.
- [class func archiveRootObject(Any, toFile: String) -> Bool](./archiverootobject%28_,tofile%29.md)
  Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.
- [func encodeRootObject(Any)](./encoderootobject%28_%29.md)
  Archives a given object along with all the objects to which it is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/encodeconditionalobject(_:))*