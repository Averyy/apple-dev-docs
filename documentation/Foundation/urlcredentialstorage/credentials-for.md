# credentials(for:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary containing the credentials for the specified protection space.

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
func credentials(for space: URLProtectionSpace) -> [String : URLCredential]?
```

#### Return Value

A dictionary containing the credentials for the specified protection space. The dictionary’s keys are user name strings, and each value is the corresponding [`URLCredential`](urlcredential.md).

#### Discussion

If you override this method, also override [`getCredentials(for:task:completionHandler:)`](urlcredentialstorage/getcredentials(for:task:completionhandler:).md).

## Parameters

- `space`: The protection space whose credentials you want to retrieve.

## See Also

- [var allCredentials: [URLProtectionSpace : [String : URLCredential]]](urlcredentialstorage/allcredentials.md)
  The credentials for all available protection spaces.
- [func getCredentials(for: URLProtectionSpace, task: URLSessionTask, completionHandler: ([String : URLCredential]?) -> Void)](urlcredentialstorage/getcredentials(for:task:completionhandler:).md)
  Gets a dictionary containing the credentials for the specified protection space, on behalf of the given task, and passes the dictionary to the provided completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredentialstorage/credentials(for:))*