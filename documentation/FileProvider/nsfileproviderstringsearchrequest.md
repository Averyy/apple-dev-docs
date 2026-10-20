# NSFileProviderStringSearchRequest

**Framework**: File Provider  
**Kind**: class  
**Role**: Class

A type that contains details of a string-based search request.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class NSFileProviderStringSearchRequest
```

```objc
@interface NSFileProviderStringSearchRequest : NSObject
```

## Topics

### Working with request properties
- [var query: String](./nsfileproviderstringsearchrequest/query.md)
  A plaintext string, representing the query a person entered into the system search UI.
### Instance Properties
- [var desiredNumberOfResults: Int](./nsfileproviderstringsearchrequest/desirednumberofresults.md)
  How many results the system is requesting. This is a hint to the extension, to help avoid unnecessary work. The extension may return more results than this.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Implementing search
- [func searchEnumerator(for: NSFileProviderStringSearchRequest) -> any NSFileProviderSearchEnumerator](./nsfileprovidersearching/searchenumerator%28for%29.md)
  Provides an object that enumerates over search results, in response to a call from the system.
- [protocol NSFileProviderSearchEnumerator](./nsfileprovidersearchenumerator.md)
  A protocol that defines methods for providing search results and canceling searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderstringsearchrequest)*