# isInline

**Framework**: CrashReportExtension  
**Kind**: property

A flag that indicates if the stack frame is inline.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let isInline: Bool
```

## See Also

- [let sourceFile: String?](symbolicatedframe/sourcefile.md)
  The name of the source file, if available.
- [let sourceLine: Int?](symbolicatedframe/sourceline.md)
  The line number within the source file, if available.
- [let symbol: String](symbolicatedframe/symbol.md)
  The symbol associated with the stack frame.
- [let symbolOffset: UInt64](symbolicatedframe/symboloffset.md)
  The symbol offset within the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/symbolicatedframe/isinline)*