# major

**Framework**: Core Location  
**Kind**: property

The constraint’s value for the major identity characteristic.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+

## Declaration

```swift
var major: UInt16? { get }
```

#### Discussion

The major characteristic is optional. If it’s present, a beacon’s major value needs to match the constraint’s major value to represent a match. If the constraint has no major value, it acts as a wildcard and matches any major value. You can specify the major value when initializing the constraint.

## See Also

- [var minor: UInt16?](clbeaconidentityconstraint/minor.md)
  The constraint’s value for the minor identity characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconidentityconstraint/major)*