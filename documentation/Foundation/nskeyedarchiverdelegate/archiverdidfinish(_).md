# archiverDidFinish(_:)

**Framework**: Foundation  
**Kind**: method

Notifies the delegate that encoding has finished.

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
optional func archiverDidFinish(_ archiver: NSKeyedArchiver)
```

## Parameters

- `archiver`: The archiver that sent the message.

## See Also

- [func archiver(NSKeyedArchiver, didEncode: Any?)](nskeyedarchiverdelegate/archiver(_:didencode:).md)
  Informs the delegate that a given object has been encoded.
- [func archiver(NSKeyedArchiver, willEncode: Any) -> Any?](nskeyedarchiverdelegate/archiver(_:willencode:).md)
  Informs the delegate that `object` is about to be encoded.
- [func archiverWillFinish(NSKeyedArchiver)](nskeyedarchiverdelegate/archiverwillfinish(_:).md)
  Notifies the delegate that encoding is about to finish.
- [func archiver(NSKeyedArchiver, willReplace: Any?, with: Any?)](nskeyedarchiverdelegate/archiver(_:willreplace:with:).md)
  Informs the delegate that one given object is being substituted for another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiverdidfinish(_:))*