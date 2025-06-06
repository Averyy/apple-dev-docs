# size()

**Framework**: Assets Library  
**Kind**: method

Returns the size in bytes of the file for the representation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func size() -> Int64
```

#### Return Value

The size  in bytes of the file for the representation.

#### Discussion

You typically use this method to allocate a buffer of the right size for [`getBytes(_:fromOffset:length:error:)`](alassetrepresentation/getbytes(_:fromoffset:length:error:).md).

## See Also

- [func getBytes(UnsafeMutablePointer<UInt8>!, fromOffset: Int64, length: Int, error: NSErrorPointer) -> Int](alassetrepresentation/getbytes(_:fromoffset:length:error:).md)
  Copies a specified range of bytes into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/size())*