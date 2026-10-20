# remove(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the specified credential from the credential storage for the specified protection space.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func remove(_ credential: URLCredential, for space: URLProtectionSpace)
```

```objc
- (void) removeCredential:(NSURLCredential *) credential forProtectionSpace:(NSURLProtectionSpace *) space;
```

#### Discussion

If you override this method, also override [`remove(_:for:options:task:)`](./remove%28_,for,options,task%29.md).

## Parameters

- `credential`: The credential to remove.
- `space`: The protection space from which to remove the credential.

## See Also

### Adding and removing credentials
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?)](./remove%28_,for,options%29.md)
  Removes the specified credential from the credential storage for the specified protection space using the given options.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?, task: URLSessionTask)](./remove%28_,for,options,task%29.md)
  Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md)
  Key used by the options dictionary passed in [`remove(_:for:options:)`](./remove%28_,for,options%29.md).
- [func set(URLCredential, for: URLProtectionSpace)](./set%28_,for%29.md)
  Adds a credential to the credential storage for the specified protection space.
- [func set(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](./set%28_,for,task%29.md)
  Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/remove(_:for:))*