# sourceFile

**Framework**: CrashReportExtension  
**Kind**: property  
**Role**: Instance Property

The name of the source file, if available.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
let sourceFile: String?
```

## See Also

### Accessing symbolicated frame properties
- [let sourceLine: Int?](./sourceline.md)
  The line number within the source file, if available.
- [let symbol: String](./symbol.md)
  The symbol associated with the stack frame.
- [let symbolOffset: UInt64](./symboloffset.md)
  The symbol offset within the frame.
- [let isInline: Bool](./isinline.md)
  A flag that indicates if the stack frame is inline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/symbolicatedframe/sourcefile)*