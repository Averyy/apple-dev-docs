# getDataValue()

**Framework**: IOBluetooth  
**Kind**: method

If the data element is represented by a data object, it returns the value as an NSData.

**Availability**:
- macOS ?+

## Declaration

```swift
func getDataValue() -> Data!
```

#### Return Value

Returns an NSData representation of the data element if it is a 128-bit number.

#### Discussion

The data types represented by a data object are 128-bit versions of 1 (unsigned int) and 2 (signed int).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/getdatavalue())*