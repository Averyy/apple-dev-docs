# persistentReference

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns a persistent reference to store a reference to an identity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var persistentReference: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * persistentReference;
```

## Return Value

A data object that uniquely references an identity.

## Discussion

A persistent reference data object is an object generated from an identity. Persistent data objects can be written to and read from a file, making them extremely useful for storing identities in an ACL.

## See Also

### Storing Identities
- [CSIdentity](./csidentity.md)
  Returns an opaque object for use with the Core Services Identity API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/persistentreference)*