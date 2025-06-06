# CFDataAppendBytes(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Appends the bytes from a byte buffer to the contents of a CFData object.

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
func CFDataAppendBytes(_ theData: CFMutableData!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex)
```

## Parameters

- `theData`: A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.
- `bytes`: A pointer to the buffer of bytes to be added to  .
- `length`: The number of bytes in the byte buffer  .

## See Also

- [func CFDataDeleteBytes(CFMutableData!, CFRange)](cfdatadeletebytes(_:_:).md)
  Deletes the bytes in a CFMutableData object within a specified range.
- [func CFDataReplaceBytes(CFMutableData!, CFRange, UnsafePointer<UInt8>!, CFIndex)](cfdatareplacebytes(_:_:_:_:).md)
  Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [func CFDataIncreaseLength(CFMutableData!, CFIndex)](cfdataincreaselength(_:_:).md)
  Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [func CFDataSetLength(CFMutableData!, CFIndex)](cfdatasetlength(_:_:).md)
  Resets the length of a CFMutableData object’s internal byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdataappendbytes(_:_:_:))*