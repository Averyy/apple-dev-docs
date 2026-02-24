# ResponseErrorInfo

**Framework**: Device Management  
**Kind**: dictionary

Information about the error.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ResponseErrorInfo
```

## Topics

### Objects and Data Types
- [object Asset](asset.md)
  A product in the store.

## Properties

- `assets` ([Asset]): The requested assets that result in an error.
- `clientUserIds` ([string]): The requested users that result in an error.
- `serialNumbers` ([string]): The requested devices that result in an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/responseerrorinfo)*