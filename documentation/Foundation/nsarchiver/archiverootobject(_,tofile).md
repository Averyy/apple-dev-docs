# archiveRootObject(_:toFile:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
class func archiveRootObject(_ rootObject: Any, toFile path: String) -> Bool
```

```objc
+ (BOOL) archiveRootObject:(id) rootObject toFile:(NSString *) path;
```

#### Return Value

[`true`](../../Swift/true.md) if the archive was written successfully, otherwise [`false`](../../Swift/false.md).

#### Discussion

This convenience method invokes [`archivedData(withRootObject:)`](./archiveddata%28withrootobject%29.md) to get the encoded data, and then sends that data object the message [`write(toFile:atomically:)`](../nsdata/write%28tofile,atomically%29.md), using `path` for the first argument and [`true`](../../Swift/true.md) for the second.

The archived data should be retrieved from the archive by an [`NSUnarchiver`](../nsunarchiver.md) object.

## Parameters

- `rootObject`: The root object of the object graph to archive.
- `path`: The location of the file into which to write the archive.

## See Also

### Related Documentation
- [func write(toFile: String, atomically: Bool) -> Bool](../nsdata/write%28tofile,atomically%29.md)
  Writes the data object’s bytes to the file specified by a given path.
### Archiving data
- [class func archivedData(withRootObject: Any) -> Data](./archiveddata%28withrootobject%29.md)
  Returns a data object containing the encoded form of the object graph whose root object is given.
- [func encodeRootObject(Any)](./encoderootobject%28_%29.md)
  Archives a given object along with all the objects to which it is connected.
- [func encodeConditionalObject(Any?)](./encodeconditionalobject%28_%29.md)
  Conditionally archives a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/archiverootobject(_:tofile:))*