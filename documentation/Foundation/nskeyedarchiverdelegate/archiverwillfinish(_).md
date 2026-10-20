# archiverWillFinish(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that encoding is about to finish.

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
optional func archiverWillFinish(_ archiver: NSKeyedArchiver)
```

```objc
- (void) archiverWillFinish:(NSKeyedArchiver *) archiver;
```

## Parameters

- `archiver`: The archiver that sent the message.

## See Also

### Encoding Data and Objects
- [func archiver(NSKeyedArchiver, didEncode: Any?)](./archiver%28_,didencode%29.md)
  Informs the delegate that a given object has been encoded.
- [func archiverDidFinish(NSKeyedArchiver)](./archiverdidfinish%28_%29.md)
  Notifies the delegate that encoding has finished.
- [func archiver(NSKeyedArchiver, willEncode: Any) -> Any?](./archiver%28_,willencode%29.md)
  Informs the delegate that `object` is about to be encoded.
- [func archiver(NSKeyedArchiver, willReplace: Any?, with: Any?)](./archiver%28_,willreplace,with%29.md)
  Informs the delegate that one given object is being substituted for another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiverwillfinish(_:))*