# hashValue

**Framework**: IdentityDocumentServices  
**Kind**: property

The hash value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values aren’t guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**:  `hashValue` is deprecated as a `Hashable` requirement. Instead, to conform to `Hashable`, implement the `hash(into:)` requirement. The compiler provides an implementation for `hashValue` for you.

## See Also

- [func hash(into: inout Hasher)](identitydocumentwebpresentmenterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func == (IdentityDocumentWebPresentmentError, IdentityDocumentWebPresentmentError) -> Bool](identitydocumentwebpresentmenterror/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmenterror/hashvalue)*