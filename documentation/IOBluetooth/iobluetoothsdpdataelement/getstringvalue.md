# getStringValue()

**Framework**: IOBluetooth  
**Kind**: method

If the data element is represented by a string object, it returns the value as an NSString.

**Availability**:
- macOS ?+

## Declaration

```swift
func getStringValue() -> String!
```

#### Return Value

Returns an NSString representation of the data element if it is a text or URL type.

#### Discussion

The data types represented by a string object are 4 (text string) and 8 (URL).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/getstringvalue())*