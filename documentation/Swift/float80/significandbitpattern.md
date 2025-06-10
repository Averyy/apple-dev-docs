# significandBitPattern

**Framework**: Swift  
**Kind**: property

The raw encoding of the value’s significand field.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var significandBitPattern: UInt64 { get }
```

#### Discussion

The `significandBitPattern` property does not include the leading integral bit of the significand, even for types like `Float80` that store it explicitly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/significandbitpattern)*