# isEqual(to:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Method for determining CWNetwork object equality.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func isEqual(to network: CWNetwork) -> Bool
```

```objc
- (BOOL) isEqualToNetwork:(CWNetwork *) network;
```

## Return Value

*YES* if the objects are equal.

## Discussion

Two CWNetwork objects are considered equal if their corresponding *ssidData*, *securityType*, and *networkType* properties are equal.

## Parameters

- `network`: The CWNetwork object for which to test equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetwork/isequal(to:))*