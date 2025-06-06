# isXIDStart

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a starting position in a programming language identifier, with adjustments made for NFKC normalized form.

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
var isXIDStart: Bool { get }
```

#### Discussion

The set of scalars `[:XID_Start:]` closes the set `[:ID_Start:]` under NFKC normalization by removing any scalars whose normalized form is not of the form `[:ID_Start:] [:ID_Continue:]*`.

This property corresponds to the “XID_Start” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isxidstart)*