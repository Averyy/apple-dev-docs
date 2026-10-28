# isEqual(to:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Determine CWNetworkProfile object equality.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func isEqual(to networkProfile: CWNetworkProfile) -> Bool
```

```objc
- (BOOL) isEqualToNetworkProfile:(CWNetworkProfile *) networkProfile;
```

## Return Value

*YES* if the objects are equal.

## Discussion

CWNetwork objects are considered equal if their corresponding *ssidData* and *securityType* properties are equal.

## Parameters

- `networkProfile`: The CWNetworkProfile object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/isequal(to:))*