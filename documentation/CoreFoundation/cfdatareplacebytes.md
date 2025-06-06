# CFDataReplaceBytes(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.

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
func CFDataReplaceBytes(_ theData: CFMutableData!, _ range: CFRange, _ newBytes: UnsafePointer<UInt8>!, _ newLength: CFIndex)
```

## Parameters

- `theData`: A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.
- `range`: The range of bytes (that is, the starting byte and the number of bytes from that point) to delete from  ’s byte buffer.
- `newBytes`: A pointer to the buffer containing the replacement bytes.
- `newLength`: The number of bytes in the byte buffer  .

## See Also

- [func CFDataAppendBytes(CFMutableData!, UnsafePointer<UInt8>!, CFIndex)](cfdataappendbytes(_:_:_:).md)
  Appends the bytes from a byte buffer to the contents of a CFData object.
- [func CFDataDeleteBytes(CFMutableData!, CFRange)](cfdatadeletebytes(_:_:).md)
  Deletes the bytes in a CFMutableData object within a specified range.
- [func CFDataIncreaseLength(CFMutableData!, CFIndex)](cfdataincreaselength(_:_:).md)
  Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [func CFDataSetLength(CFMutableData!, CFIndex)](cfdatasetlength(_:_:).md)
  Resets the length of a CFMutableData object’s internal byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatareplacebytes(_:_:_:_:))*