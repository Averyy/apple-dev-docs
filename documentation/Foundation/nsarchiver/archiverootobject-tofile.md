# archiveRootObject(_:toFile:)

**Framework**: Foundation  
**Kind**: method

Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func archiveRootObject(_ rootObject: Any, toFile path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the archive was written successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This convenience method invokes [`archivedData(withRootObject:)`](nsarchiver/archiveddata(withrootobject:).md) to get the encoded data, and then sends that data object the message [`write(toFile:atomically:)`](nsdata/write(tofile:atomically:).md), using `path` for the first argument and [`true`](https://developer.apple.com/documentation/Swift/true) for the second.

The archived data should be retrieved from the archive by an [`NSUnarchiver`](nsunarchiver.md) object.

## Parameters

- `rootObject`: The root object of the object graph to archive.
- `path`: The location of the file into which to write the archive.

## See Also

- [func write(toFile: String, atomically: Bool) -> Bool](nsdata/write(tofile:atomically:).md)
  Writes the data object’s bytes to the file specified by a given path.
- [class func archivedData(withRootObject: Any) -> Data](nsarchiver/archiveddata(withrootobject:).md)
  Returns a data object containing the encoded form of the object graph whose root object is given.
- [func encodeRootObject(Any)](nsarchiver/encoderootobject(_:).md)
  Archives a given object along with all the objects to which it is connected.
- [func encodeConditionalObject(Any?)](nsarchiver/encodeconditionalobject(_:).md)
  Conditionally archives a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/archiverootobject(_:tofile:))*