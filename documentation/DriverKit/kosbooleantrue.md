# kOSBooleanTrue

**Framework**: DriverKit  
**Kind**: var  
**Role**: Global Variable

The OSBoolean constant for `true` .

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
extern OSBooleanPtr kOSBooleanTrue;
```

#### Discussion

kOSBooleanTrue is the OSBoolean constant for `true` . This object does not need to be retained or released (but it can be). Comparisons should be of the form `booleanObject == kOSBooleanTrue`

## See Also

### Getting Boolean Values
- [kOSBooleanFalse](./kosbooleanfalse.md)
  The OSBoolean constant for `false` .


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/kosbooleantrue)*