# replaceBytes(in:withBytes:)

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
func replaceBytes(in range: NSRange, withBytes bytes: UnsafeRawPointer)
```

#### Discussion

If the location of `range` isn’t within the receiver’s range of bytes, an `NSRangeException` is raised. The receiver is resized to accommodate the new bytes, if necessary.

A sample using this method is given in [`Working With Mutable Binary Data`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingMutableData.html#//apple_ref/doc/uid/20002150).

## Parameters

- `range`: The range within the receiver’s contents to replace with  . The range must not exceed the bounds of the receiver.
- `bytes`: The data to insert into the receiver’s contents.

## See Also

- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer?, length: Int)](nsmutabledata/replacebytes(in:withbytes:length:).md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func resetBytes(in: NSRange)](nsmutabledata/resetbytes(in:).md)
  Replaces with zeroes the contents of the receiver in a given range.
- [func setData(Data)](nsmutabledata/setdata(_:).md)
  Replaces the entire contents of the receiver with the contents of another data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/replacebytes(in:withbytes:))*