# encodeRootObject(_:)

**Framework**: Foundation  
**Kind**: method

Archives a given object along with all the objects to which it is connected.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func encodeRootObject(_ rootObject: Any)
```

#### Discussion

If any object is encountered more than once while traversing the graph, it is encoded only once, but the multiple references to it are stored. (See [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) for more information.)

This message must not be sent more than once to a given `NSArchiver` object; an `NSInvalidArgumentException` is raised if a root object has already been encoded. If you need to encode multiple object graphs, therefore, don’t attempt to reuse an `NSArchiver` instance; instead, create a new one for each graph.

## Parameters

- `rootObject`: The root object of the object graph to archive.

## See Also

- [class func archivedData(withRootObject: Any) -> Data](nsarchiver/archiveddata(withrootobject:).md)
  Returns a data object containing the encoded form of the object graph whose root object is given.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nsarchiver/archiverootobject(_:tofile:).md)
  Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.
- [func encodeConditionalObject(Any?)](nsarchiver/encodeconditionalobject(_:).md)
  Conditionally archives a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/encoderootobject(_:))*