# sourceLine

**Framework**: CrashReportExtension  
**Kind**: property

The line number within the source file, if available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let sourceLine: Int?
```

## See Also

- [let sourceFile: String?](symbolicatedframe/sourcefile.md)
  The name of the source file, if available.
- [let symbol: String](symbolicatedframe/symbol.md)
  The symbol associated with the stack frame.
- [let symbolOffset: UInt64](symbolicatedframe/symboloffset.md)
  The symbol offset within the frame.
- [let isInline: Bool](symbolicatedframe/isinline.md)
  A flag that indicates if the stack frame is inline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/symbolicatedframe/sourceline)*