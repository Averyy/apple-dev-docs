# cString(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a representation of the string as a C string using a given encoding.

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
func cString(using encoding: UInt) -> UnsafePointer<CChar>?
```

```objc
- (const char *) cStringUsingEncoding:(NSStringEncoding) encoding;
```

## Return Value

A C string representation of the receiver using the encoding specified by `encoding`. Returns `NULL` if the receiver cannot be losslessly converted to `encoding`.

## Discussion

The returned C string is guaranteed to be valid only until either the receiver is freed, or until the current memory is emptied, whichever occurs first. You should copy the C string or use [`getCString(_:maxLength:encoding:)`](./getcstring%28_,maxlength,encoding%29.md) if it needs to store the C string beyond this time.

You can use [`canBeConverted(to:)`](./canbeconverted%28to%29.md) to check whether a string can be losslessly converted to `encoding`. If it can’t, you can use [`data(using:allowLossyConversion:)`](./data%28using,allowlossyconversion%29.md) to get a C-string representation using `encoding`, allowing some loss of information (note that the data returned by [`data(using:allowLossyConversion:)`](./data%28using,allowlossyconversion%29.md) is not a strict C-string since it does not have a `NULL` terminator).

### Special Considerations

UTF-16 and UTF-32 are not considered to be C string encodings, and should not be used with this method—the results of passing [`NSUTF16StringEncoding`](../nsutf16stringencoding.md), [`NSUTF32StringEncoding`](../nsutf32stringencoding.md), or any of their variants are undefined.

## Parameters

- `encoding`: The encoding for the returned C string. For possible values, see [`NSStringEncoding`](../nsstringencoding.md).

## See Also

### Related Documentation
- [func canBeConverted(to: UInt) -> Bool](./canbeconverted%28to%29.md)
  Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [func getCString(UnsafeMutablePointer<CChar>)](./getcstring%28_%29.md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](./getcstring%28_,maxlength,range,remaining%29.md) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [func cStringLength() -> Int](./cstringlength%28%29.md)
  Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.
- [class var defaultCStringEncoding: UInt](./defaultcstringencoding.md)
  Returns the C-string encoding assumed for any method accepting a C string as an argument.
### Getting C Strings
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int, encoding: UInt) -> Bool](./getcstring%28_,maxlength,encoding%29.md)
  Converts the string to a given encoding and stores it in a buffer.
- [var utf8String: UnsafePointer<CChar>?](./utf8string.md)
  A null-terminated UTF8 representation of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/cstring(using:))*