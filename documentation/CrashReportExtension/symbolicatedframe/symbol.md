# symbol

**Framework**: CrashReportExtension  
**Kind**: property

The symbol associated with the stack frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let symbol: String
```

## See Also

- [let sourceFile: String?](symbolicatedframe/sourcefile.md)
  The name of the source file, if available.
- [let sourceLine: Int?](symbolicatedframe/sourceline.md)
  The line number within the source file, if available.
- [let symbolOffset: UInt64](symbolicatedframe/symboloffset.md)
  The symbol offset within the frame.
- [let isInline: Bool](symbolicatedframe/isinline.md)
  A flag that indicates if the stack frame is inline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/symbolicatedframe/symbol)*