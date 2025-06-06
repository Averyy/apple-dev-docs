# contains(_:)

**Framework**: IOBluetooth  
**Kind**: method

Checks to see if the target data element is the same as the dataElement parameter or if it contains the dataElement parameter (if its a sequence type).

**Availability**:
- macOS ?+

## Declaration

```swift
func contains(_ dataElement: IOBluetoothSDPDataElement!) -> Bool
```

#### Return Value

Returns TRUE if the target either matches the given data element or if it contains the given data element.

#### Discussion

If the target data element is not a sequence type, this method simply compares the two data elements. If it is a sequence type, it will search through the sequence (and sub-sequences) for the dataElement parameter.

## Parameters

- `dataElement`: The data element to compare with (and search for).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/contains(_:))*