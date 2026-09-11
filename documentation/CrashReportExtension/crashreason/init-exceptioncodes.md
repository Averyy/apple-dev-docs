# init(exception:codes:)

**Framework**: CrashReportExtension  
**Kind**: init

Creates a crash reason instance with the given parameters.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(exception: Int32, codes: [UInt64])
```

## Parameters

- `exception`: The Mach exception type.
- `codes`: An array of exception-specific codes providing additional details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashreason/init(exception:codes:))*