# isSubnormal

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the instance is subnormal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isSubnormal: Bool { get }
```

#### Discussion

A  value is a nonzero number that has a lesser magnitude than the smallest normal number. Subnormal values don’t use the full precision available to values of a type.

Zero is neither a normal nor a subnormal number. Subnormal numbers are often called  or —these are different names for the same concept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/issubnormal)*