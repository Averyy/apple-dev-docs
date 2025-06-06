# CFDataSetLength(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Resets the length of a CFMutableData object’s internal byte buffer.

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
func CFDataSetLength(_ theData: CFMutableData!, _ length: CFIndex)
```

#### Discussion

This function resets the length of a CFMutableData object’s underlying byte buffer to a new size. If that size is less than the current size, it truncates the excess bytes. If that size is greater than the current size, it zero-fills the extension to the byte buffer.

## Parameters

- `theData`: A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.
- `length`: The new size of  ’s byte buffer.

## See Also

- [func CFDataAppendBytes(CFMutableData!, UnsafePointer<UInt8>!, CFIndex)](cfdataappendbytes(_:_:_:).md)
  Appends the bytes from a byte buffer to the contents of a CFData object.
- [func CFDataDeleteBytes(CFMutableData!, CFRange)](cfdatadeletebytes(_:_:).md)
  Deletes the bytes in a CFMutableData object within a specified range.
- [func CFDataReplaceBytes(CFMutableData!, CFRange, UnsafePointer<UInt8>!, CFIndex)](cfdatareplacebytes(_:_:_:_:).md)
  Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [func CFDataIncreaseLength(CFMutableData!, CFIndex)](cfdataincreaselength(_:_:).md)
  Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatasetlength(_:_:))*