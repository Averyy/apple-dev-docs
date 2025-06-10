# URLCredentialStorage

**Framework**: Foundation  
**Kind**: class

The manager of a shared credentials cache.

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
class URLCredentialStorage
```

#### Overview

The shared cache stores and retrieves instances of [`URLCredential`](urlcredential.md). You can store password-based credentials permanently, based on the [`URLCredential.Persistence`](urlcredential/persistence-swift.enum.md) they were created with. Certificate-based credentials are never stored permanently.

##### Subclassing Notes

The [`URLCredentialStorage`](urlcredentialstorage.md) class is meant to be used as-is, but you can subclass it if you have specific needs, such as screening which credentials are stored.

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred to equivalent methods that do not. Therefore, you should override the task-based methods when subclassing, as follows:

- Setting credentials — Override [`set(_:for:task:)`](urlcredentialstorage/set(_:for:task:).md) instead of or in addition to [`set(_:for:)`](urlcredentialstorage/set(_:for:).md).
- Getting credentials — Override [`getCredentials(for:task:completionHandler:)`](urlcredentialstorage/getcredentials(for:task:completionhandler:).md) instead of or in addition to [`credentials(for:)`](urlcredentialstorage/credentials(for:).md).
- Removing credentials — Override [`remove(_:for:options:task:)`](urlcredentialstorage/remove(_:for:options:task:).md) instead of or in addition to [`remove(_:for:options:)`](urlcredentialstorage/remove(_:for:options:).md) and [`remove(_:for:)`](urlcredentialstorage/remove(_:for:).md).
- Setting default credentials — Override [`setDefaultCredential(_:for:task:)`](urlcredentialstorage/setdefaultcredential(_:for:task:).md) instead of or in addition to [`setDefaultCredential(_:for:)`](urlcredentialstorage/setdefaultcredential(_:for:).md).
- Getting default credentials — Override [`getDefaultCredential(for:task:completionHandler:)`](urlcredentialstorage/getdefaultcredential(for:task:completionhandler:).md) instead of or in addition to [`defaultCredential(for:)`](urlcredentialstorage/defaultcredential(for:).md).

## Topics

### Getting the credential storage
- [class var shared: URLCredentialStorage](urlcredentialstorage/shared.md)
  The shared URL credential storage instance.
### Getting and setting default credentials
- [func defaultCredential(for: URLProtectionSpace) -> URLCredential?](urlcredentialstorage/defaultcredential(for:).md)
  Returns the default credential for the specified protection space.
- [func getDefaultCredential(for: URLProtectionSpace, task: URLSessionTask, completionHandler: (URLCredential?) -> Void)](urlcredentialstorage/getdefaultcredential(for:task:completionhandler:).md)
  Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/setdefaultcredential(_:for:).md)
  Sets the default credential for a specified protection space.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/setdefaultcredential(_:for:task:).md)
  Sets the default credential for a given protection space, which is being accessed by the given task.
### Adding and removing credentials
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
- [func set(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/set(_:for:task:).md)
  Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.
### Retrieving credentials
- [var allCredentials: [URLProtectionSpace : [String : URLCredential]]](urlcredentialstorage/allcredentials.md)
  The credentials for all available protection spaces.
- [func credentials(for: URLProtectionSpace) -> [String : URLCredential]?](urlcredentialstorage/credentials(for:).md)
  Returns a dictionary containing the credentials for the specified protection space.
- [func getCredentials(for: URLProtectionSpace, task: URLSessionTask, completionHandler: ([String : URLCredential]?) -> Void)](urlcredentialstorage/getcredentials(for:task:completionhandler:).md)
  Gets a dictionary containing the credentials for the specified protection space, on behalf of the given task, and passes the dictionary to the provided completion handler.
### Tracking credential storage changes
- [static let NSURLCredentialStorageChanged: NSNotification.Name](nsnotification/name-swift.struct/nsurlcredentialstoragechanged.md)
  A notification posted when the set of stored credentials changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Handling an authentication challenge](handling-an-authentication-challenge.md)
  Respond appropriately when a server demands authentication for a URL request.
- [class URLAuthenticationChallenge](urlauthenticationchallenge.md)
  A challenge from a server requiring authentication from the client.
- [class URLCredential](urlcredential.md)
  `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [class URLProtectionSpace](urlprotectionspace.md)
  A server or an area on a server, commonly referred to as a realm, that requires authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage)*