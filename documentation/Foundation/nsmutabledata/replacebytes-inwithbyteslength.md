# replaceBytes(in:withBytes:length:)

**Framework**: Foundation  
**Kind**: method

Replaces with a given set of bytes a given range within the contents of the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func replaceBytes(in range: NSRange, withBytes replacementBytes: UnsafeRawPointer?, length replacementLength: Int)
```

#### Discussion

If the length of `range` is not equal to `replacementLength`, the receiver is resized to accommodate the new bytes. Any bytes past `range` in the receiver are shifted to accommodate the new bytes. You can therefore pass `NULL` for `replacementBytes` and `0` for `replacementLength` to delete bytes in the receiver in the range `range`. You can also replace a range (which might be zero-length) with more bytes than the length of the range, which has the effect of insertion (or “replace some and insert more”).

## Parameters

- `range`: The range within the receiver’s contents to replace with  . The range must not exceed the bounds of the receiver.
- `replacementBytes`: The data to insert into the receiver’s contents.
- `replacementLength`: The number of bytes to take from  .

## See Also

- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer)](nsmutabledata/replacebytes(in:withbytes:).md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func resetBytes(in: NSRange)](nsmutabledata/resetbytes(in:).md)
  Replaces with zeroes the contents of the receiver in a given range.
- [func setData(Data)](nsmutabledata/setdata(_:).md)
  Replaces the entire contents of the receiver with the contents of another data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/replacebytes(in:withbytes:length:))*