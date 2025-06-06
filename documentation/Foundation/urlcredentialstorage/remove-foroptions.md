# remove(_:for:options:)

**Framework**: Foundation  
**Kind**: method

Removes the specified credential from the credential storage for the specified protection space using the given options.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func remove(_ credential: URLCredential, for space: URLProtectionSpace, options: [String : Any]? = nil)
```

#### Discussion

The credential is removed from both persistent and temporary storage.

If you override this method, also override [`remove(_:for:options:task:)`](urlcredentialstorage/remove(_:for:options:task:).md).

## Parameters

- `credential`: The credential to remove.
- `space`: The protection space from which to remove the credential.
- `options`: For possible keys, see  . You should use this when trying to delete a credential that has the   policy.

## See Also

- [func remove(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/remove(_:for:).md)
  Removes the specified credential from the credential storage for the specified protection space.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?, task: URLSessionTask)](urlcredentialstorage/remove(_:for:options:task:).md)
  Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](dictionary-key-for-credential-removal-options.md)
  Key used by the options dictionary passed in [`remove(_:for:options:)`](urlcredentialstorage/remove(_:for:options:).md).
- [func set(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/set(_:for:).md)
  Adds a credential to the credential storage for the specified protection space.
- [func set(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/set(_:for:task:).md)
  Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/remove(_:for:options:))*