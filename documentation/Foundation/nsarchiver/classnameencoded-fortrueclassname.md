# classNameEncoded(forTrueClassName:)

**Framework**: Foundation  
**Kind**: method

Returns the name of the class used to archive instances of the class with a given true name.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func classNameEncoded(forTrueClassName trueName: String) -> String?
```

#### Return Value

The name of the class used to archive instances of the class `trueName`.

## Parameters

- `trueName`: The real name of an encoded class.

## See Also

- [func encodeClassName(String, intoClassName: String)](nsarchiver/encodeclassname(_:intoclassname:).md)
  Encodes a substitute name for the class with a given true name.
- [func replace(Any, with: Any)](nsarchiver/replace(_:with:).md)
  Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/classnameencoded(fortrueclassname:))*