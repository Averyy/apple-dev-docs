# archivedData(withRootObject:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a data object containing the encoded form of the object graph whose root object is given.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
class func archivedData(withRootObject rootObject: Any) -> Data
```

```objc
+ (NSData *) archivedDataWithRootObject:(id) rootObject;
```

## Return Value

A data object containing the encoded form of the object graph whose root object is `rootObject`.

## Discussion

This method invokes [`init(forWritingWith:)`](./init%28forwritingwith%29.md) and [`encodeRootObject(_:)`](./encoderootobject%28_%29.md) to create a temporary archiver that encodes the object graph.

## Parameters

- `rootObject`: The root object of the object graph to archive.

## See Also

### Related Documentation
- [init(forWritingWith: NSMutableData)](./init%28forwritingwith%29.md)
  Returns an archiver, initialized to encode stream and version information into a given mutable data object.
### Archiving data
- [class func archiveRootObject(Any, toFile: String) -> Bool](./archiverootobject%28_,tofile%29.md)
  Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.
- [func encodeRootObject(Any)](./encoderootobject%28_%29.md)
  Archives a given object along with all the objects to which it is connected.
- [func encodeConditionalObject(Any?)](./encodeconditionalobject%28_%29.md)
  Conditionally archives a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/archiveddata(withrootobject:))*