# exception

**Framework**: CrashReportExtension  
**Kind**: property

The Mach exception type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let exception: Int32
```

#### Discussion

Possible values of this property include `EXC_BAD_ACCESS` and `EXC_CRASH`.

## See Also

- [let codes: [UInt64]](crashreason/codes.md)
  An array of exception-specific codes providing additional details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashreason/exception)*