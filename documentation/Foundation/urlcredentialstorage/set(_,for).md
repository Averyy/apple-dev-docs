# set(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a credential to the credential storage for the specified protection space.

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
func set(_ credential: URLCredential, for space: URLProtectionSpace)
```

```objc
- (void) setCredential:(NSURLCredential *) credential forProtectionSpace:(NSURLProtectionSpace *) space;
```

## Discussion

If the credential is not yet in the set for the protection space, it will be added to it.

If you override this method, also override [`set(_:for:task:)`](./set%28_,for,task%29.md).

## Parameters

- `credential`: The credential to add. If a credential with the same user name already exists in `space`, then `credential` replaces the existing object.
- `space`: The protection space to which to add the credential.

## See Also

### Adding and removing credentials
- [func remove(URLCredential, for: URLProtectionSpace)](./remove%28_,for%29.md)
  Removes the specified credential from the credential storage for the specified protection space.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?)](./remove%28_,for,options%29.md)
  Removes the specified credential from the credential storage for the specified protection space using the given options.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?, task: URLSessionTask)](./remove%28_,for,options,task%29.md)
  Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md)
  Key used by the options dictionary passed in [`remove(_:for:options:)`](./remove%28_,for,options%29.md).
- [func set(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](./set%28_,for,task%29.md)
  Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/set(_:for:))*