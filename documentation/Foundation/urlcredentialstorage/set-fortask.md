# set(_:for:task:)

**Framework**: Foundation  
**Kind**: method

Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

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
func set(_ credential: URLCredential, for protectionSpace: URLProtectionSpace, task: URLSessionTask)
```

## Parameters

- `credential`: The credential to add. If a credential with the same user name already exists in  , then   replaces the existing object.
- `protectionSpace`: The protection space to which to add the credential.
- `task`: The task accessing the specified protection space. Subclasses of   may use the request URL or other properties of this task to affect how the default credential is stored.

## See Also

- [func remove(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/remove(_:for:).md)
  Removes the specified credential from the credential storage for the specified protection space.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?)](urlcredentialstorage/remove(_:for:options:).md)
  Removes the specified credential from the credential storage for the specified protection space using the given options.
- [func remove(URLCredential, for: URLProtectionSpace, options: [String : Any]?, task: URLSessionTask)](urlcredentialstorage/remove(_:for:options:task:).md)
  Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](dictionary-key-for-credential-removal-options.md)
  Key used by the options dictionary passed in [`remove(_:for:options:)`](urlcredentialstorage/remove(_:for:options:).md).
- [func set(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/set(_:for:).md)
  Adds a credential to the credential storage for the specified protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/set(_:for:task:))*