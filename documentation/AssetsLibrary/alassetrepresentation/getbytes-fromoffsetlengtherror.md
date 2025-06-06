# getBytes(_:fromOffset:length:error:)

**Framework**: Assets Library  
**Kind**: method

Copies a specified range of bytes into a given buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func getBytes(_ buffer: UnsafeMutablePointer<UInt8>!, fromOffset offset: Int64, length: Int, error: NSErrorPointer) -> Int
```

#### Return Value

The number of bytes actually written to `buffer`. The number of bytes read will be less than the requested range if the range exceeds the file’s size. If an error occurs, returns `0`.

#### Discussion

This method returns the biggest, best representation available.

> **Note**:  In iOS 8 and later, use the Photos framework to access different versions and sizes of a photo asset. See [`PHImageManager`](https://developer.apple.com/documentation/Photos/PHImageManager).

 In iOS 8 and later, use the Photos framework to access different versions and sizes of a photo asset. See [`PHImageManager`](https://developer.apple.com/documentation/Photos/PHImageManager).

## Parameters

- `buffer`: You typically use   to allocate a buffer of the right size.
- `offset`: The number of bytes from the beginning of the file to start copying.
- `length`: The number of bytes to copy.
- `error`: Pass   if you do not want error information.

## See Also

- [func size() -> Int64](alassetrepresentation/size.md)
  Returns the size in bytes of the file for the representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/getbytes(_:fromoffset:length:error:))*