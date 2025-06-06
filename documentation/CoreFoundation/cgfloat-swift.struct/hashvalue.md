# hashValue

**Framework**: Corefoundation  
**Kind**: property

The hash value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS ?+
- watchOS 1.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

 `x == y` implies `x.hashValue == y.hashValue`.

> **Note**:  The hash value is not guaranteed to be stable across different invocations of the same program.  Do not persist the hash value across program runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreFoundation/cgfloat-swift.struct/hashvalue)*