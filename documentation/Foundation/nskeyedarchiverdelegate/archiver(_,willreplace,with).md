# archiver(_:willReplace:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) archiver:(NSKeyedArchiver *) archiver willReplaceObject:(id) object withObject:(id) newObject;
```

## Discussion

This method is called even when the delegate itself is doing, or has done, the substitution. The delegate may use this method if it is keeping track of the encoded or decoded objects.

## Parameters

- `archiver`: The archiver that sent the message.
- `object`: The object being replaced in the archive.
- `newObject`: The object replacing `object` in the archive.

## See Also

### Encoding Data and Objects
- [func archiver(NSKeyedArchiver, didEncode: Any?)](./archiver%28_,didencode%29.md)
  Informs the delegate that a given object has been encoded.
- [func archiverDidFinish(NSKeyedArchiver)](./archiverdidfinish%28_%29.md)
  Notifies the delegate that encoding has finished.
- [func archiver(NSKeyedArchiver, willEncode: Any) -> Any?](./archiver%28_,willencode%29.md)
  Informs the delegate that `object` is about to be encoded.
- [func archiverWillFinish(NSKeyedArchiver)](./archiverwillfinish%28_%29.md)
  Notifies the delegate that encoding is about to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiver(_:willreplace:with:))*