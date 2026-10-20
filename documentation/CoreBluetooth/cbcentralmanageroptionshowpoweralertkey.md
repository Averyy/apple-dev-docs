# CBCentralManagerOptionShowPowerAlertKey

**Framework**: Core Bluetooth  
**Kind**: var  
**Role**: Global Variable

A Boolean value that specifies whether the system warns the user if the app instantiates the central manager when Bluetooth service isn’t available.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBCentralManagerOptionShowPowerAlertKey: String
```

```c
extern NSString * const CBCentralManagerOptionShowPowerAlertKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../Foundation/nsnumber.md) object. If the key isn’t specified, the default value is [`true`](../Swift/true.md).

## See Also

### Constants
- [let CBCentralManagerOptionRestoreIdentifierKey: String](./cbcentralmanageroptionrestoreidentifierkey.md)
  A string containing a unique identifier (UID) for the central manager to instantiate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanageroptionshowpoweralertkey)*