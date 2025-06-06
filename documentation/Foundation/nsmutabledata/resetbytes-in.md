# resetBytes(in:)

**Framework**: Foundation  
**Kind**: method

Replaces with zeroes the contents of the receiver in a given range.

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
func resetBytes(in range: NSRange)
```

#### Discussion

If the location of `range` isn’t within the receiver’s range of bytes, an `NSRangeException` is raised. The receiver is resized to accommodate the new bytes, if necessary.

## Parameters

- `range`: The range within the contents of the receiver to be replaced by zeros. The range must not exceed the bounds of the receiver.

## See Also

- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer)](nsmutabledata/replacebytes(in:withbytes:).md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer?, length: Int)](nsmutabledata/replacebytes(in:withbytes:length:).md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func setData(Data)](nsmutabledata/setdata(_:).md)
  Replaces the entire contents of the receiver with the contents of another data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/resetbytes(in:))*