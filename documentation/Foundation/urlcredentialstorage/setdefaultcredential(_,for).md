# setDefaultCredential(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setDefaultCredential:(NSURLCredential *) credential forProtectionSpace:(NSURLProtectionSpace *) space;
```

## Discussion

If you override this method, also override [`setDefaultCredential(_:for:task:)`](./setdefaultcredential%28_,for,task%29.md).

## Parameters

- `credential`: The URL credential to set as the default for `space`. If the receiver does not contain `credential` in the specified protection space it will be added.
- `space`: The protection space whose default credential is being set.

## See Also

### Getting and setting default credentials
- [func defaultCredential(for: URLProtectionSpace) -> URLCredential?](./defaultcredential%28for%29.md)
  Returns the default credential for the specified protection space.
- [func getDefaultCredential(for: URLProtectionSpace, task: URLSessionTask, completionHandler: (URLCredential?) -> Void)](./getdefaultcredential%28for,task,completionhandler%29.md)
  Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](./setdefaultcredential%28_,for,task%29.md)
  Sets the default credential for a given protection space, which is being accessed by the given task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:))*