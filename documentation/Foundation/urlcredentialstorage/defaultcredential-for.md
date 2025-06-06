# defaultCredential(for:)

**Framework**: Foundation  
**Kind**: method

Returns the default credential for the specified protection space.

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
func defaultCredential(for space: URLProtectionSpace) -> URLCredential?
```

#### Return Value

The default credential for `space` or `nil` if no default has been set.

#### Discussion

If you override this method, also override [`getDefaultCredential(for:task:completionHandler:)`](urlcredentialstorage/getdefaultcredential(for:task:completionhandler:).md).

## Parameters

- `space`: The URL protection space of interest.

## See Also

- [func getDefaultCredential(for: URLProtectionSpace, task: URLSessionTask, completionHandler: (URLCredential?) -> Void)](urlcredentialstorage/getdefaultcredential(for:task:completionhandler:).md)
  Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace)](urlcredentialstorage/setdefaultcredential(_:for:).md)
  Sets the default credential for a specified protection space.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](urlcredentialstorage/setdefaultcredential(_:for:task:).md)
  Sets the default credential for a given protection space, which is being accessed by the given task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/defaultcredential(for:))*