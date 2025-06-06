# archiver(_:didEncode:)

**Framework**: Foundation  
**Kind**: method

Informs the delegate that a given object has been encoded.

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
optional func archiver(_ archiver: NSKeyedArchiver, didEncode object: Any?)
```

#### Discussion

The delegate might restore some state it had modified previously, or use this opportunity to keep track of the objects that are encoded.

This method is not called for conditional objects until they are actually encoded (if ever).

## Parameters

- `archiver`: The archiver that sent the message.
- `object`: The object that has been encoded.   may be  .

## See Also

- [Archives and Serializations Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [func archiverDidFinish(NSKeyedArchiver)](nskeyedarchiverdelegate/archiverdidfinish(_:).md)
  Notifies the delegate that encoding has finished.
- [func archiver(NSKeyedArchiver, willEncode: Any) -> Any?](nskeyedarchiverdelegate/archiver(_:willencode:).md)
  Informs the delegate that `object` is about to be encoded.
- [func archiverWillFinish(NSKeyedArchiver)](nskeyedarchiverdelegate/archiverwillfinish(_:).md)
  Notifies the delegate that encoding is about to finish.
- [func archiver(NSKeyedArchiver, willReplace: Any?, with: Any?)](nskeyedarchiverdelegate/archiver(_:willreplace:with:).md)
  Informs the delegate that one given object is being substituted for another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiver(_:didencode:))*