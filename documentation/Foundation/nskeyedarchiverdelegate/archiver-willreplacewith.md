# archiver(_:willReplace:with:)

**Framework**: Foundation  
**Kind**: method

Informs the delegate that one given object is being substituted for another given object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func archiver(_ archiver: NSKeyedArchiver, willReplace object: Any?, with newObject: Any?)
```

#### Discussion

This method is called even when the delegate itself is doing, or has done, the substitution. The delegate may use this method if it is keeping track of the encoded or decoded objects.

## Parameters

- `archiver`: The archiver that sent the message.
- `object`: The object being replaced in the archive.
- `newObject`: The object replacing   in the archive.

## See Also

- [func archiver(NSKeyedArchiver, didEncode: Any?)](nskeyedarchiverdelegate/archiver(_:didencode:).md)
  Informs the delegate that a given object has been encoded.
- [func archiverDidFinish(NSKeyedArchiver)](nskeyedarchiverdelegate/archiverdidfinish(_:).md)
  Notifies the delegate that encoding has finished.
- [func archiver(NSKeyedArchiver, willEncode: Any) -> Any?](nskeyedarchiverdelegate/archiver(_:willencode:).md)
  Informs the delegate that `object` is about to be encoded.
- [func archiverWillFinish(NSKeyedArchiver)](nskeyedarchiverdelegate/archiverwillfinish(_:).md)
  Notifies the delegate that encoding is about to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiver(_:willreplace:with:))*