# setDefaultCredential(_:for:)

**Framework**: Foundation  
**Kind**: method

Sets the default credential for a specified protection space.

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
func setDefaultCredential(_ credential: URLCredential, for space: URLProtectionSpace)
```

#### Discussion

If you override this method, also override [`setDefaultCredential(_:for:task:)`](urlcredentialstorage/setdefaultcredential(_:for:task:).md).

## Parameters

- `credential`: The URL credential to set as the default for  . If the receiver does not contain   in the specified protection space it will be added.
- `space`: The protection space whose default credential is being set.

## See Also

- [func defaultCredential(for: URLProtectionSpace) -> URLCredential?](urlcredentialstorage/defaultcredential(for:).md)
  Returns the default credential for the specified protection space.
- [func getDefaultCredential(for: URLProtectionSpace, task: URLSessionTask, completionHandler: (URLCredential?) -> Void)](urlcredentialstorage/getdefaultcredential(for:task:completionhandler:).md)
  Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/setdefaultcredential(_:for:task:).md)
  Sets the default credential for a given protection space, which is being accessed by the given task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:))*