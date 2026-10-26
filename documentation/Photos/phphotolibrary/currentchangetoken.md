# currentChangeToken

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The opaque token that represents the current state of the Photos library.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var currentChangeToken: PHPersistentChangeToken { get }
```

```objc
@property (nonatomic, readonly) PHPersistentChangeToken * currentChangeToken;
```

## See Also

### Fetching Change History
- [func fetchPersistentChanges(since: PHPersistentChangeToken) throws -> PHPersistentChangeFetchResult](./fetchpersistentchanges%28since%29.md)
  Retrieves the Photos library changes since the token you specify.
- [class PHPersistentChangeFetchResult](../phpersistentchangefetchresult.md)
  An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [class PHPersistentChangeToken](../phpersistentchangetoken.md)
  An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/currentchangetoken)*