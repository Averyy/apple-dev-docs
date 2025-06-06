# setDefaultCredential(_:for:task:)

**Framework**: Foundation  
**Kind**: method

Sets the default credential for a given protection space, which is being accessed by the given task.

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
func setDefaultCredential(_ credential: URLCredential, for protectionSpace: URLProtectionSpace, task: URLSessionTask)
```

## Parameters

- `credential`: The URL credential to set as the default for the protection space. If the receiver does not contain   in the specified protection space it will be added.
- `protectionSpace`: The protection space whose default credential is being set.
- `task`: The task accessing the specified protection space. Subclasses of   may use the request URL or other properties of this task to affect how the default credential is stored.

## See Also

- [func defaultCredential(for: URLProtectionSpace) -> URLCredential?](urlcredentialstorage/defaultcredential(for:).md)
  Returns the default credential for the specified protection space.
- [func getDefaultCredential(for: URLProtectionSpace, task: URLSessionTask, completionHandler: (URLCredential?) -> Void)](urlcredentialstorage/getdefaultcredential(for:task:completionhandler:).md)
  Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/setdefaultcredential(_:for:).md)
  Sets the default credential for a specified protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:task:))*