# archivedData(withRootObject:)

**Framework**: Foundation  
**Kind**: method

Returns a data object containing the encoded form of the object graph whose root object is given.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func archivedData(withRootObject rootObject: Any) -> Data
```

#### Return Value

A data object containing the encoded form of the object graph whose root object is `rootObject`.

#### Discussion

This method invokes [`init(forWritingWith:)`](nsarchiver/init(forwritingwith:).md) and [`encodeRootObject(_:)`](nsarchiver/encoderootobject(_:).md) to create a temporary archiver that encodes the object graph.

## Parameters

- `rootObject`: The root object of the object graph to archive.

## See Also

- [init(forWritingWith: NSMutableData)](nsarchiver/init(forwritingwith:).md)
  Returns an archiver, initialized to encode stream and version information into a given mutable data object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nsarchiver/archiverootobject(_:tofile:).md)
  Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.
- [func encodeRootObject(Any)](nsarchiver/encoderootobject(_:).md)
  Archives a given object along with all the objects to which it is connected.
- [func encodeConditionalObject(Any?)](nsarchiver/encodeconditionalobject(_:).md)
  Conditionally archives a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/archiveddata(withrootobject:))*