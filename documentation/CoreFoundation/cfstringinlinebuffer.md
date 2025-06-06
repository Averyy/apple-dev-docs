# CFStringInlineBuffer

**Framework**: Core Foundation  
**Kind**: struct

Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFStringInlineBuffer
```

#### Overview

This structure is used for in-line buffer access of characters contained by a CFString object. Use the [`CFStringInitInlineBuffer(_:_:_:)`](cfstringinitinlinebuffer(_:_:_:).md) function for initializing the fields of this structure; do not do it manually. Once the buffer is initialized, use the [`CFStringGetCharacterFromInlineBuffer(_:_:)`](cfstringgetcharacterfrominlinebuffer(_:_:).md) function to access characters from the buffer. Do not access the fields directly as they might change between releases.

The only reason this structure is not opaque is to allow the in-line functions to access its fields.

## Topics

### Initializers
- [init()](cfstringinlinebuffer/init.md)
- [init(buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar), theString: Unmanaged<CFString>!, directUniCharBuffer: UnsafePointer<UniChar>!, directCStringBuffer: UnsafePointer<CChar>!, rangeToBuffer: CFRange, bufferedRangeStart: CFIndex, bufferedRangeEnd: CFIndex)](cfstringinlinebuffer/init(buffer:thestring:directunicharbuffer:directcstringbuffer:rangetobuffer:bufferedrangestart:bufferedrangeend:).md)
### Instance Properties
- [var buffer: (UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar, UniChar)](cfstringinlinebuffer/buffer.md)
- [var bufferedRangeEnd: CFIndex](cfstringinlinebuffer/bufferedrangeend.md)
- [var bufferedRangeStart: CFIndex](cfstringinlinebuffer/bufferedrangestart.md)
- [var directCStringBuffer: UnsafePointer<CChar>!](cfstringinlinebuffer/directcstringbuffer.md)
- [var directUniCharBuffer: UnsafePointer<UniChar>!](cfstringinlinebuffer/directunicharbuffer.md)
- [var rangeToBuffer: CFRange](cfstringinlinebuffer/rangetobuffer.md)
- [var theString: Unmanaged<CFString>!](cfstringinlinebuffer/thestring.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias CFStringEncoding](cfstringencoding.md)
  An integer type for constants used to specify supported string encodings in various CFString functions.
- [enum CFStringEncodings](cfstringencodings.md)
  Index type for constants used to specify external string encodings.
- [struct CFStringCompareFlags](cfstringcompareflags.md)
  A [`CFOptionFlags`](cfoptionflags.md) type for specifying options for string comparison .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringinlinebuffer)*