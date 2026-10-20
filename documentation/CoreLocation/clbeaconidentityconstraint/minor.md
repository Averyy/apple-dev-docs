# minor

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The constraint’s value for the minor identity characteristic.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+

## Declaration

```swift
var minor: UInt16? { get }
```

#### Discussion

The minor characteristic is optional. If it’s present, a beacon’s minor value needs to match the constraint’s minor value to represent a match. If the constraint has no minor value, it acts as a wildcard and matches any minor value.

## See Also

### Getting the beacon identity
- [var major: UInt16?](./major.md)
  The constraint’s value for the major identity characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconidentityconstraint/minor)*