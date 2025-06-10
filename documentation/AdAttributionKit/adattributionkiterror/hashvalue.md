# hashValue

**Framework**: AdAttributionKit  
**Kind**: property

The hash value.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/adattributionkiterror/hashvalue)*