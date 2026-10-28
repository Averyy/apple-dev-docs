# CFDataIncreaseLength(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDataIncreaseLength(_ theData: CFMutableData!, _ extraLength: CFIndex)
```

```c
extern void CFDataIncreaseLength(CFMutableDataRef theData, CFIndex extraLength);
```

## Discussion

This function increases the length of a CFMutableData object’s underlying byte buffer to a new size, initializing the new bytes to `0`.

## Parameters

- `theData`: A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.
- `extraLength`: The number of bytes by which to increase the byte buffer.

## See Also

### Modifying a Mutable Data Object
- [func CFDataAppendBytes(CFMutableData!, UnsafePointer<UInt8>!, CFIndex)](./cfdataappendbytes%28_,_,_%29.md)
  Appends the bytes from a byte buffer to the contents of a CFData object.
- [func CFDataDeleteBytes(CFMutableData!, CFRange)](./cfdatadeletebytes%28_,_%29.md)
  Deletes the bytes in a CFMutableData object within a specified range.
- [func CFDataReplaceBytes(CFMutableData!, CFRange, UnsafePointer<UInt8>!, CFIndex)](./cfdatareplacebytes%28_,_,_,_%29.md)
  Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [func CFDataSetLength(CFMutableData!, CFIndex)](./cfdatasetlength%28_,_%29.md)
  Resets the length of a CFMutableData object’s internal byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdataincreaselength(_:_:))*