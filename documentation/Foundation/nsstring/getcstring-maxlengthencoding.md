# getCString(_:maxLength:encoding:)

**Framework**: Foundation  
**Kind**: method

Converts the string to a given encoding and stores it in a buffer.

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
func getCString(_ buffer: UnsafeMutablePointer<CChar>, maxLength maxBufferCount: Int, encoding: UInt) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation was successful, otherwise [`false`](https://developer.apple.com/documentation/swift/false). Returns [`false`](https://developer.apple.com/documentation/swift/false) if conversion is not possible due to encoding errors or if `buffer` is too small.

#### Discussion

Note that in the treatment of the `maxBufferCount` argument, this method differs from the deprecated [`getCString(_:maxLength:)`](nsstring/getcstring(_:maxlength:).md) method which it replaces. (The buffer should include room for `maxBufferCount` bytes; this number should accommodate the expected size of the return value plus the `NULL` termination byte, which this method adds.)

You can use [`canBeConverted(to:)`](nsstring/canbeconverted(to:).md) to check whether a string can be losslessly converted to `encoding`. If it can’t, you can use [`data(using:allowLossyConversion:)`](nsstring/data(using:allowlossyconversion:).md) to get a C-string representation using `encoding`, allowing some loss of information (note that the data returned by [`data(using:allowLossyConversion:)`](nsstring/data(using:allowlossyconversion:).md) is not a strict C-string since it does not have a `NULL` terminator).

## Parameters

- `buffer`: Upon return, contains the converted C-string plus the   termination byte. The buffer must include room for   bytes.
- `maxBufferCount`: The maximum number of bytes in the string to return in buffer (  the   termination byte).
- `encoding`: The encoding for the returned C string. For possible values, see  .

## See Also

- [func canBeConverted(to: UInt) -> Bool](nsstring/canbeconverted(to:).md)
  Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [func cString(using: UInt) -> UnsafePointer<CChar>?](nsstring/cstring(using:).md)
  Returns a representation of the string as a C string using a given encoding.
- [var utf8String: UnsafePointer<CChar>?](nsstring/utf8string.md)
  A null-terminated UTF8 representation of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getcstring(_:maxlength:encoding:))*