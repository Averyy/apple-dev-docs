# valid

**Framework**: Security  
**Kind**: property

The code is dynamically valid.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var valid: SecCodeStatus { get }
```

#### Discussion

Code that’s dynamically valid is running code that started properly signed and has not been invalidated since it started. The valid bit can not be set on running code; it can only be cleared. If you do not set the `kSecCodeStatusValid` flag during creation of the guest with the [`SecCodeGetTypeID()`](seccodegettypeid().md) function, then the new guest is created dynamically invalid and can never become dynamically valid. Note that this bit does not make any representations about the static validity of the code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodestatus/valid)*