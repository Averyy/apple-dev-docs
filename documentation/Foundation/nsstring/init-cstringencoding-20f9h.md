# init(cString:encoding:)

**Framework**: Foundation  
**Kind**: init

Returns an @c NSString object initialized using the characters in a given C array, interpreted according to a given encoding.

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
convenience init?(cString nullTerminatedCString: UnsafePointer<CChar>, encoding: UInt)
```

#### Return Value

An @c NSString object initialized using the characters from @c nullTerminatedCString. The returned object may be different from the original receiver.

## Parameters

- `nullTerminatedCString`: A C array of characters. The array must end with a @c NULL character; intermediate @c NULL characters are not allowed.
- `encoding`: The encoding of @c nullTerminatedCString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(cstring:encoding:)-20f9h)*