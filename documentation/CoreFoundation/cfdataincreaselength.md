# CFDataIncreaseLength(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.

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
func CFDataIncreaseLength(_ theData: CFMutableData!, _ extraLength: CFIndex)
```

#### Discussion

This function increases the length of a CFMutableData object’s underlying byte buffer to a new size, initializing the new bytes to `0`.

## Parameters

- `theData`: A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.
- `extraLength`: The number of bytes by which to increase the byte buffer.

## See Also

- [func CFDataAppendBytes(CFMutableData!, UnsafePointer<UInt8>!, CFIndex)](cfdataappendbytes(_:_:_:).md)
  Appends the bytes from a byte buffer to the contents of a CFData object.
- [func CFDataDeleteBytes(CFMutableData!, CFRange)](cfdatadeletebytes(_:_:).md)
  Deletes the bytes in a CFMutableData object within a specified range.
- [func CFDataReplaceBytes(CFMutableData!, CFRange, UnsafePointer<UInt8>!, CFIndex)](cfdatareplacebytes(_:_:_:_:).md)
  Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [func CFDataSetLength(CFMutableData!, CFIndex)](cfdatasetlength(_:_:).md)
  Resets the length of a CFMutableData object’s internal byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdataincreaselength(_:_:))*