# isDebuggable

**Framework**: LightweightCodeRequirements  
**Kind**: property

Flag indicating that the process is debuggable by authorized debuggers.

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
static let isDebuggable: ProcessCodeSigningFlags.ValueSet
```

#### Discussion

This is equivalent to `CS_GET_TASK_ALLOW` in C APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags/valueset/isdebuggable)*