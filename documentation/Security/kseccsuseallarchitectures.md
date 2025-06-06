# kSecCSUseAllArchitectures

**Framework**: Security  
**Kind**: var

Flag for requesting all architectures.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecCSUseAllArchitectures: UInt32 { get }
```

#### Discussion

When this flag is used, if code refers to a single architecture of a universal binary, return a [`SecStaticCode`](secstaticcode.md) object that refers to the entire universal code with all its architectures. By default, the returned static reference identifies only the actual architecture of the running program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccsuseallarchitectures)*