# signalsBusErrorOnCodeSigningFailure

**Framework**: LightweightCodeRequirements  
**Kind**: property

Code signing failures on page-in should be rejected as SIGBUS errors.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static let signalsBusErrorOnCodeSigningFailure: OnDiskCodeSigningFlags.ValueSet
```

#### Discussion

This flag may be present on any on disk signature. This flag only has effect on main executables. This is equivalent to `CS_HARD` in C APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset/signalsbuserroroncodesigningfailure)*