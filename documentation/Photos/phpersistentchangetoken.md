# PHPersistentChangeToken

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class PHPersistentChangeToken
```

```objc
@interface PHPersistentChangeToken : NSObject
```

## Mentions

- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)

## Topics

### Initializers
- [init?(coder: NSCoder)](./phpersistentchangetoken/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Fetching Change History
- [func fetchPersistentChanges(since: PHPersistentChangeToken) throws -> PHPersistentChangeFetchResult](./phphotolibrary/fetchpersistentchanges%28since%29.md)
  Retrieves the Photos library changes since the token you specify.
- [class PHPersistentChangeFetchResult](./phpersistentchangefetchresult.md)
  An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [var currentChangeToken: PHPersistentChangeToken](./phphotolibrary/currentchangetoken.md)
  The opaque token that represents the current state of the Photos library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentchangetoken)*