# encodeRootObject(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Archives a given object along with all the objects to which it is connected.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
func encodeRootObject(_ rootObject: Any)
```

```objc
- (void) encodeRootObject:(id) rootObject;
```

## Discussion

If any object is encountered more than once while traversing the graph, it is encoded only once, but the multiple references to it are stored. (See [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) for more information.)

This message must not be sent more than once to a given `NSArchiver` object; an `NSInvalidArgumentException` is raised if a root object has already been encoded. If you need to encode multiple object graphs, therefore, don’t attempt to reuse an `NSArchiver` instance; instead, create a new one for each graph.

## Parameters

- `rootObject`: The root object of the object graph to archive.

## See Also

### Archiving data
- [class func archivedData(withRootObject: Any) -> Data](./archiveddata%28withrootobject%29.md)
  Returns a data object containing the encoded form of the object graph whose root object is given.
- [class func archiveRootObject(Any, toFile: String) -> Bool](./archiverootobject%28_,tofile%29.md)
  Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.
- [func encodeConditionalObject(Any?)](./encodeconditionalobject%28_%29.md)
  Conditionally archives a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/encoderootobject(_:))*