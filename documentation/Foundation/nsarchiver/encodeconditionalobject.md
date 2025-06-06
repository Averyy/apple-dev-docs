# encodeConditionalObject(_:)

**Framework**: Foundation  
**Kind**: method

Conditionally archives a given object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func encodeConditionalObject(_ object: Any?)
```

#### Discussion

This method overrides the superclass implementation to allow `object` to be encoded only if it is also encoded unconditionally by another object in the object graph. Conditional encoding lets you encode one part of a graph detached from the rest. (See [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) for more information.)

This method should be invoked only from within an [`encode(with:)`](nscoding/encode(with:).md) method. If `object` is `nil`, the `NSArchiver` object encodes it unconditionally as `nil`. This method raises an `NSInvalidArgumentException` if no root object has been encoded.

## Parameters

- `object`: The object to archive.

## See Also

- [class func archivedData(withRootObject: Any) -> Data](nsarchiver/archiveddata(withrootobject:).md)
  Returns a data object containing the encoded form of the object graph whose root object is given.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nsarchiver/archiverootobject(_:tofile:).md)
  Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.
- [func encodeRootObject(Any)](nsarchiver/encoderootobject(_:).md)
  Archives a given object along with all the objects to which it is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/encodeconditionalobject(_:))*