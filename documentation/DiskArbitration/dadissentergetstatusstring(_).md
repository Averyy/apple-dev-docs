# DADissenterGetStatusString(_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Obtains the return code string.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADissenterGetStatusString(_ dissenter: DADissenter) -> CFString?
```

```c
extern CFStringRefDADissenterGetStatusString(DADissenterRef dissenter);
```

#### Return Value

The return code string.

## Parameters

- `dissenter`: The DADissenter for which to obtain the return code string.

## See Also

### Miscellaneous
- [func DADissenterCreate(CFAllocator?, DAReturn, CFString?) -> DADissenter](./dadissentercreate%28_,_,_%29.md)
  Creates a new dissenter object.
- [func DADissenterGetStatus(DADissenter) -> DAReturn](./dadissentergetstatus%28_%29.md)
  Obtains the return code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadissentergetstatusstring(_:))*