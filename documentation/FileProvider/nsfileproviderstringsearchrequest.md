# NSFileProviderStringSearchRequest

**Framework**: File Provider  
**Kind**: class

A type that contains details of a string-based search request.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
class NSFileProviderStringSearchRequest
```

## Topics

### Working with request properties
- [var query: String](nsfileproviderstringsearchrequest/query.md)
  A plaintext string, representing the query a person entered into the system search UI.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func searchEnumerator(for: NSFileProviderStringSearchRequest) -> any NSFileProviderSearchEnumerator](nsfileprovidersearching/searchenumerator(for:).md)
  Provides an object that enumerates over search results, in response to a call from the system.
- [protocol NSFileProviderSearchEnumerator](nsfileprovidersearchenumerator.md)
  A protocol that defines methods for providing search results and canceling searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderstringsearchrequest)*