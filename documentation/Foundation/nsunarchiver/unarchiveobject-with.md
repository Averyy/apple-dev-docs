# unarchiveObject(with:)

**Framework**: Foundation  
**Kind**: method

Decodes and returns the object archived in a given `NSData` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func unarchiveObject(with data: Data) -> Any?
```

#### Return Value

The object, or object graph, that was archived in `data`. Returns `nil` if `data` cannot be unarchived.

#### Discussion

This method invokes [`init(forReadingWith:)`](nsunarchiver/init(forreadingwith:).md) and [`decodeObject()`](nscoder/decodeobject().md) to create a temporary `NSUnarchiver` object that decodes the object. If the archived object is the root of a graph of objects, the entire graph is unarchived.

## Parameters

- `data`: An   object that contains an archive created using  .

## See Also

- [func encodeRootObject(Any)](nsarchiver/encoderootobject(_:).md)
  Archives a given object along with all the objects to which it is connected.
- [class func unarchiveObject(withFile: String) -> Any?](nsunarchiver/unarchiveobject(withfile:).md)
  Decodes and returns the object archived in the file `path`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/unarchiveobject(with:))*