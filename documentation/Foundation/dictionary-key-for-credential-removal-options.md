# Dictionary key for credential removal options

**Framework**: Foundation  
**Role**: API Collection

Key used by the options dictionary passed in [`remove(_:for:options:)`](./urlcredentialstorage/remove%28_,for,options%29.md).

## Topics

### Options
- [let NSURLCredentialStorageRemoveSynchronizableCredentials: String](./nsurlcredentialstorageremovesynchronizablecredentials.md)
  The corresponding value is an `NSNumber` object representing a Boolean value that indicates whether credentials which contain the [`URLCredential.Persistence.synchronizable`](./urlcredential/persistence-swift.enum/synchronizable.md) attribute should be removed.

## See Also

### Adding and removing credentials
- [func remove(URLCredential, for: URLProtectionSpace)](./urlcredentialstorage/remove%28_,for%29.md)
  Removes the specified credential from the credential storage for the specified protection space.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?)](./urlcredentialstorage/remove%28_,for,options%29.md)
  Removes the specified credential from the credential storage for the specified protection space using the given options.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?, task: URLSessionTask)](./urlcredentialstorage/remove%28_,for,options,task%29.md)
  Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [func set(URLCredential, for: URLProtectionSpace)](./urlcredentialstorage/set%28_,for%29.md)
  Adds a credential to the credential storage for the specified protection space.
- [func set(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](./urlcredentialstorage/set%28_,for,task%29.md)
  Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dictionary-key-for-credential-removal-options)*