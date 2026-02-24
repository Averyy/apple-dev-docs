# remove(_:for:options:task:)

**Framework**: Foundation  
**Kind**: method

Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func remove(_ credential: URLCredential, for protectionSpace: URLProtectionSpace, options: [String : Any]? = nil, task: URLSessionTask)
```

#### Discussion

The credential is removed from both persistent and temporary storage.

## Parameters

- `credential`: The credential to remove.
- `protectionSpace`: The protection space from which to remove the credential.
- `options`: A dictionary containing options to consider when removing the credential. For possible keys, see [`Dictionary key for credential removal options`](dictionary-key-for-credential-removal-options.md). You should use this when trying to delete a credential that has the [`URLCredential.Persistence.synchronizable`](urlcredential/persistence-swift.enum/synchronizable.md) policy. > **Note**:  When credential objects that have a `synchronizable` policy are removed, the credential will be removed on all devices that contain this credential.
- `task`: The task using the protection space that you wish to remove the credential for.

## See Also

- [func remove(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/remove(_:for:).md)
  Removes the specified credential from the credential storage for the specified protection space.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?)](urlcredentialstorage/remove(_:for:options:).md)
  Removes the specified credential from the credential storage for the specified protection space using the given options.
- [Dictionary key for credential removal options](dictionary-key-for-credential-removal-options.md)
  Key used by the options dictionary passed in [`remove(_:for:options:)`](urlcredentialstorage/remove(_:for:options:).md).
- [func set(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/set(_:for:).md)
  Adds a credential to the credential storage for the specified protection space.
- [func set(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/set(_:for:task:).md)
  Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/remove(_:for:options:task:))*