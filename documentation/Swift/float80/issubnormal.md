# isSubnormal

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the instance is subnormal.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isSubnormal: Bool { get }
```

#### Discussion

A  value is a nonzero number that has a lesser magnitude than the smallest normal number. Subnormal values don’t use the full precision available to values of a type.

Zero is neither a normal nor a subnormal number. Subnormal numbers are often called  or —these are different names for the same concept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/issubnormal)*