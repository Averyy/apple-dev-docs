# allCredentials

**Framework**: Foundation  
**Kind**: property

The credentials for all available protection spaces.

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
var allCredentials: [URLProtectionSpace : [String : URLCredential]] { get }
```

#### Discussion

The dictionary has keys corresponding to the [`URLProtectionSpace`](urlprotectionspace.md) instances. The values are dictionaries where the keys are user name strings, and each value is the corresponding [`URLCredential`](urlcredential.md) instances.

## See Also

- [func credentials(for: URLProtectionSpace) -> [String : URLCredential]?](urlcredentialstorage/credentials(for:).md)
  Returns a dictionary containing the credentials for the specified protection space.
- [func getCredentials(for: URLProtectionSpace, task: URLSessionTask, completionHandler: ([String : URLCredential]?) -> Void)](urlcredentialstorage/getcredentials(for:task:completionhandler:).md)
  Gets a dictionary containing the credentials for the specified protection space, on behalf of the given task, and passes the dictionary to the provided completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/allcredentials)*