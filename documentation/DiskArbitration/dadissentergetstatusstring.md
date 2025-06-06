# DADissenterGetStatusString(_:)

**Framework**: Disk Arbitration  
**Kind**: func

Obtains the return code string.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADissenterGetStatusString(_ dissenter: DADissenter) -> CFString?
```

#### Return Value

The return code string.

## Parameters

- `dissenter`: The DADissenter for which to obtain the return code string.

## See Also

- [func DADissenterCreate(CFAllocator?, DAReturn, CFString?) -> DADissenter](dadissentercreate(_:_:_:).md)
  Creates a new dissenter object.
- [func DADissenterGetStatus(DADissenter) -> DAReturn](dadissentergetstatus(_:).md)
  Obtains the return code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadissentergetstatusstring(_:))*