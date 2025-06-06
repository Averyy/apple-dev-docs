# persistentReference

**Framework**: Collaboration  
**Kind**: property

Returns a persistent reference to store a reference to an identity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var persistentReference: Data? { get }
```

#### Return Value

A data object that uniquely references an identity.

#### Discussion

A persistent reference data object is an object generated from an identity. Persistent data objects can be written to and read from a file, making them extremely useful for storing identities in an ACL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/persistentreference)*