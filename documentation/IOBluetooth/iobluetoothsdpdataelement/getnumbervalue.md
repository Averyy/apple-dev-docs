# getNumberValue()

**Framework**: IOBluetooth  
**Kind**: method

If the data element is represented by a number, it returns the value as an NSNumber.

**Availability**:
- macOS ?+

## Declaration

```swift
func getNumberValue() -> NSNumber!
```

#### Return Value

Returns an NSNumber representation of the data element if it is a numeric type.

#### Discussion

The data types represented by a number are 1 (unsigned int), 2 (signed int) and 5 (boolean) except for 128-bit versions of 1 and 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/getnumbervalue())*