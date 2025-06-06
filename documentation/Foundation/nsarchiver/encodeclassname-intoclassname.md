# encodeClassName(_:intoClassName:)

**Framework**: Foundation  
**Kind**: method

Encodes a substitute name for the class with a given true name.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func encodeClassName(_ trueName: String, intoClassName inArchiveName: String)
```

#### Discussion

Any subsequently encountered objects of class `trueName` are archived as instances of class `inArchiveName`. It is safest not to invoke this method during the archiving process (that is, within an [`encode(with:)`](nscoding/encode(with:).md) method). Instead, invoke it before [`encodeRootObject(_:)`](nsarchiver/encoderootobject(_:).md).

## Parameters

- `trueName`: The real name of a class in the object graph being archived.
- `inArchiveName`: The name of the class to use in the archive in place of  .

## See Also

- [func classNameEncoded(forTrueClassName: String) -> String?](nsarchiver/classnameencoded(fortrueclassname:).md)
  Returns the name of the class used to archive instances of the class with a given true name.
- [func replace(Any, with: Any)](nsarchiver/replace(_:with:).md)
  Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/encodeclassname(_:intoclassname:))*