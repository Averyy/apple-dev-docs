# containsValue(_:)

**Framework**: IOBluetooth  
**Kind**: method

Checks to see if the target data element’s value is the same as the value parameter or if it contains the value parameter.

**Availability**:
- macOS ?+

## Declaration

```swift
func containsValue(_ cmpValue: NSObject!) -> Bool
```

#### Return Value

Returns TRUE if the target’s value either matches the given value or if it contains the given value.

#### Discussion

This method works just like -containsDataElement: except that it is comparing the value objects directly.

## Parameters

- `cmpValue`: The value to compare with (and search for).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/containsvalue(_:))*