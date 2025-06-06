# DADissenterGetStatus(_:)

**Framework**: Disk Arbitration  
**Kind**: func

Obtains the return code.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADissenterGetStatus(_ dissenter: DADissenter) -> DAReturn
```

#### Return Value

The return code. A BSD return code, if applicable, is encoded with unix_err().

## Parameters

- `dissenter`: The DADissenter for which to obtain the return code.

## See Also

- [func DADissenterCreate(CFAllocator?, DAReturn, CFString?) -> DADissenter](dadissentercreate(_:_:_:).md)
  Creates a new dissenter object.
- [func DADissenterGetStatusString(DADissenter) -> CFString?](dadissentergetstatusstring(_:).md)
  Obtains the return code string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadissentergetstatus(_:))*