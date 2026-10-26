# PHPersistentChangeFetchResult

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that represents a fetch result and allows you to enumerate a very large set of change records.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class PHPersistentChangeFetchResult
```

```objc
@interface PHPersistentChangeFetchResult : NSObject
```

## Topics

### Performing Operations with Objects in a Fetch Request
- [class PHPersistentChange](./phpersistentchange.md)
  An object that represents a change in the Photos library, and allows for requesting local identifiers that identify the changes for a library object.
- [- enumerateChangesWithBlock:](./phpersistentchangefetchresult/enumeratechangeswithblock_.md)
  Executes the block you specify by using the objects in the fetch result.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Fetching Change History
- [func fetchPersistentChanges(since: PHPersistentChangeToken) throws -> PHPersistentChangeFetchResult](./phphotolibrary/fetchpersistentchanges%28since%29.md)
  Retrieves the Photos library changes since the token you specify.
- [var currentChangeToken: PHPersistentChangeToken](./phphotolibrary/currentchangetoken.md)
  The opaque token that represents the current state of the Photos library.
- [class PHPersistentChangeToken](./phpersistentchangetoken.md)
  An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentchangefetchresult)*