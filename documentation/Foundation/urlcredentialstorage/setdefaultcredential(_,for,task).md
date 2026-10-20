# setDefaultCredential(_:for:task:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setDefaultCredential:(NSURLCredential *) credential forProtectionSpace:(NSURLProtectionSpace *) protectionSpace task:(NSURLSessionTask *) task;
```

## Parameters

- `credential`: The URL credential to set as the default for the protection space. If the receiver does not contain `credential` in the specified protection space it will be added.
- `protectionSpace`: The protection space whose default credential is being set.
- `task`: The task accessing the specified protection space. Subclasses of [`URLCredentialStorage`](../urlcredentialstorage.md) may use the request URL or other properties of this task to affect how the default credential is stored.

## See Also

### Getting and setting default credentials
- [func defaultCredential(for: URLProtectionSpace) -> URLCredential?](./defaultcredential%28for%29.md)
  Returns the default credential for the specified protection space.
- [func getDefaultCredential(for: URLProtectionSpace, task: URLSessionTask, completionHandler: (URLCredential?) -> Void)](./getdefaultcredential%28for,task,completionhandler%29.md)
  Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace)](./setdefaultcredential%28_,for%29.md)
  Sets the default credential for a specified protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:task:))*