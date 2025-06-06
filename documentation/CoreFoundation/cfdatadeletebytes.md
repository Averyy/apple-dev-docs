# CFDataDeleteBytes(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Deletes the bytes in a CFMutableData object within a specified range.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFDataDeleteBytes(_ theData: CFMutableData!, _ range: CFRange)
```

## Parameters

- `theData`: A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.
- `range`: The range of bytes (that is, the starting byte and the number of bytes from that point) to delete from  ’s byte buffer.

## See Also

- [func CFDataAppendBytes(CFMutableData!, UnsafePointer<UInt8>!, CFIndex)](cfdataappendbytes(_:_:_:).md)
  Appends the bytes from a byte buffer to the contents of a CFData object.
- [func CFDataReplaceBytes(CFMutableData!, CFRange, UnsafePointer<UInt8>!, CFIndex)](cfdatareplacebytes(_:_:_:_:).md)
  Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [func CFDataIncreaseLength(CFMutableData!, CFIndex)](cfdataincreaselength(_:_:).md)
  Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [func CFDataSetLength(CFMutableData!, CFIndex)](cfdatasetlength(_:_:).md)
  Resets the length of a CFMutableData object’s internal byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatadeletebytes(_:_:))*