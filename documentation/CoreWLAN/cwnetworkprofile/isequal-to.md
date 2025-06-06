# isEqual(to:)

**Framework**: Core WLAN  
**Kind**: method

Determine CWNetworkProfile object equality.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func isEqual(to networkProfile: CWNetworkProfile) -> Bool
```

#### Return Value

 if the objects are equal.

#### Discussion

CWNetwork objects are considered equal if their corresponding  and  properties are equal.

## Parameters

- `networkProfile`: The CWNetworkProfile object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/isequal(to:))*