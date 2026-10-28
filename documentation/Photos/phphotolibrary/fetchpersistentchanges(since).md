# fetchPersistentChanges(since:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Retrieves the Photos library changes since the token you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fetchPersistentChanges(since token: PHPersistentChangeToken) throws -> PHPersistentChangeFetchResult
```

```objc
- (PHPersistentChangeFetchResult *) fetchPersistentChangesSinceToken:(PHPersistentChangeToken *) token error:(NSError **) error;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Return Value

A fetch result that contains library change details; otherwise, an error that indicates why the fetch fails (for example, [`PHPhotosError.Code.persistentChangeTokenExpired`](../phphotoserror-swift.struct/code/persistentchangetokenexpired.md)).

## Parameters

- `token`: The token that represents the state of the Photos library to compare against.

## See Also

### Fetching Change History
- [class PHPersistentChangeFetchResult](../phpersistentchangefetchresult.md)
  An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [var currentChangeToken: PHPersistentChangeToken](./currentchangetoken.md)
  The opaque token that represents the current state of the Photos library.
- [class PHPersistentChangeToken](../phpersistentchangetoken.md)
  An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/fetchpersistentchanges(since:))*