# symbol

**Framework**: CrashReportExtension  
**Kind**: property  
**Role**: Instance Property

The symbol associated with the stack frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
let symbol: String
```

## See Also

### Accessing symbolicated frame properties
- [let sourceFile: String?](./sourcefile.md)
  The name of the source file, if available.
- [let sourceLine: Int?](./sourceline.md)
  The line number within the source file, if available.
- [let symbolOffset: UInt64](./symboloffset.md)
  The symbol offset within the frame.
- [let isInline: Bool](./isinline.md)
  A flag that indicates if the stack frame is inline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/symbolicatedframe/symbol)*