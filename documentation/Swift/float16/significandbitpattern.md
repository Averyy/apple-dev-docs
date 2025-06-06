# significandBitPattern

**Framework**: Swift  
**Kind**: property

The raw encoding of the value’s significand field.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var significandBitPattern: UInt16 { get }
```

#### Discussion

The `significandBitPattern` property does not include the leading integral bit of the significand, even for types like `Float80` that store it explicitly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/significandbitpattern)*