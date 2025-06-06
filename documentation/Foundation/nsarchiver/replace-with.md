# replace(_:with:)

**Framework**: Foundation  
**Kind**: method

Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func replace(_ object: Any, with newObject: Any)
```

#### Discussion

Both `object` and `newObject` must be valid objects.

## Parameters

- `object`: An object in the object graph being archived.
- `newObject`: The object with which to replace   in the archive.

## See Also

- [func classNameEncoded(forTrueClassName: String) -> String?](nsarchiver/classnameencoded(fortrueclassname:).md)
  Returns the name of the class used to archive instances of the class with a given true name.
- [func encodeClassName(String, intoClassName: String)](nsarchiver/encodeclassname(_:intoclassname:).md)
  Encodes a substitute name for the class with a given true name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/replace(_:with:))*