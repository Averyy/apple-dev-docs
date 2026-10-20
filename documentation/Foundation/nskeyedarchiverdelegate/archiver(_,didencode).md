# archiver(_:didEncode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) archiver:(NSKeyedArchiver *) archiver didEncodeObject:(id) object;
```

#### Discussion

The delegate might restore some state it had modified previously, or use this opportunity to keep track of the objects that are encoded.

This method is not called for conditional objects until they are actually encoded (if ever).

## Parameters

- `archiver`: The archiver that sent the message.
- `object`: The object that has been encoded. `object` may be `nil`.

## See Also

### Related Documentation
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
### Encoding Data and Objects
- [func archiverDidFinish(NSKeyedArchiver)](./archiverdidfinish%28_%29.md)
  Notifies the delegate that encoding has finished.
- [func archiver(NSKeyedArchiver, willEncode: Any) -> Any?](./archiver%28_,willencode%29.md)
  Informs the delegate that `object` is about to be encoded.
- [func archiverWillFinish(NSKeyedArchiver)](./archiverwillfinish%28_%29.md)
  Notifies the delegate that encoding is about to finish.
- [func archiver(NSKeyedArchiver, willReplace: Any?, with: Any?)](./archiver%28_,willreplace,with%29.md)
  Informs the delegate that one given object is being substituted for another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiver(_:didencode:))*