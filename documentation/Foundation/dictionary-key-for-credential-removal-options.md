# Dictionary key for credential removal options

**Framework**: Foundation

Key used by the options dictionary passed in [`remove(_:for:options:)`](urlcredentialstorage/remove(_:for:options:).md).

## Topics

### Options
- [let NSURLCredentialStorageRemoveSynchronizableCredentials: String](nsurlcredentialstorageremovesynchronizablecredentials.md)
  The corresponding value is an `NSNumber` object representing a Boolean value that indicates whether credentials which contain the [`URLCredential.Persistence.synchronizable`](urlcredential/persistence-swift.enum/synchronizable.md) attribute should be removed.

## See Also

- [func remove(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/remove(_:for:).md)
  Removes the specified credential from the credential storage for the specified protection space.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?)](urlcredentialstorage/remove(_:for:options:).md)
  Removes the specified credential from the credential storage for the specified protection space using the given options.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?, task: URLSessionTask)](urlcredentialstorage/remove(_:for:options:task:).md)
  Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [func set(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/set(_:for:).md)
  Adds a credential to the credential storage for the specified protection space.
- [func set(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/set(_:for:task:).md)
  Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dictionary-key-for-credential-removal-options)*