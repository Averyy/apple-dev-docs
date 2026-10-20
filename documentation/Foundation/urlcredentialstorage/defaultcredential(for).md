# defaultCredential(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSURLCredential *) defaultCredentialForProtectionSpace:(NSURLProtectionSpace *) space;
```

#### Return Value

The default credential for `space` or `nil` if no default has been set.

#### Discussion

If you override this method, also override [`getDefaultCredential(for:task:completionHandler:)`](./getdefaultcredential%28for,task,completionhandler%29.md).

## Parameters

- `space`: The URL protection space of interest.

## See Also

### Getting and setting default credentials
- [func getDefaultCredential(for: URLProtectionSpace, task: URLSessionTask, completionHandler: (URLCredential?) -> Void)](./getdefaultcredential%28for,task,completionhandler%29.md)
  Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace)](./setdefaultcredential%28_,for%29.md)
  Sets the default credential for a specified protection space.
- [func setDefaultCredential(URLCredential, for: URLProtectionSpace, task: URLSessionTask)](./setdefaultcredential%28_,for,task%29.md)
  Sets the default credential for a given protection space, which is being accessed by the given task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/defaultcredential(for:))*