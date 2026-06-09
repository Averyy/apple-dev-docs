# init(utf8String:)

**Framework**: Foundation  
**Kind**: init

Returns an @c NSString object initialized by copying the characters from a given C array of UTF8-encoded bytes.

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
convenience init?(utf8String nullTerminatedCString: UnsafePointer<CChar>)
```

#### Return Value

An @c NSString object initialized by copying the bytes from @c nullTerminatedCString. The returned object may be different from the original receiver.

## Parameters

- `nullTerminatedCString`: A @c NULL-terminated C array of bytes in UTF-8 encoding. This value must not be @c NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(utf8string:)-vg2b)*