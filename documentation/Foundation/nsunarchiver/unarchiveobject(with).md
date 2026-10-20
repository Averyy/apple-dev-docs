# unarchiveObject(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes and returns the object archived in a given `NSData` object.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
class func unarchiveObject(with data: Data) -> Any?
```

```objc
+ (id) unarchiveObjectWithData:(NSData *) data;
```

#### Return Value

The object, or object graph, that was archived in `data`. Returns `nil` if `data` cannot be unarchived.

#### Discussion

This method invokes [`init(forReadingWith:)`](./init%28forreadingwith%29.md) and [`decodeObject()`](../nscoder/decodeobject%28%29.md) to create a temporary `NSUnarchiver` object that decodes the object. If the archived object is the root of a graph of objects, the entire graph is unarchived.

## Parameters

- `data`: An `NSData` object that contains an archive created using `NSArchiver`.

## See Also

### Related Documentation
- [func encodeRootObject(Any)](../nsarchiver/encoderootobject%28_%29.md)
  Archives a given object along with all the objects to which it is connected.
### Decoding objects
- [class func unarchiveObject(withFile: String) -> Any?](./unarchiveobject%28withfile%29.md)
  Decodes and returns the object archived in the file `path`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/unarchiveobject(with:))*