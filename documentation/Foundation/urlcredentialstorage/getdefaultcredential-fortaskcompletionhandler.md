# getDefaultCredential(for:task:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.

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
func defaultCredential(for space: URLProtectionSpace, task: URLSessionTask) async -> URLCredential?
```

## Parameters

- `space`: The protection space of interest.
- `task`: The task seeking to use the protection space
- `completionHandler`: A completion handler that receives the default credential as its argument, or   if there is no default credential for this combination of protection space and task.

## See Also

- [func defaultCredential(for: URLProtectionSpace) -> URLCredential?](urlcredentialstorage/defaultcredential(for:).md)
  Returns the default credential for the specified protection space.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/setdefaultcredential(_:for:).md)
  Sets the default credential for a specified protection space.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/setdefaultcredential(_:for:task:).md)
  Sets the default credential for a given protection space, which is being accessed by the given task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/getdefaultcredential(for:task:completionhandler:))*