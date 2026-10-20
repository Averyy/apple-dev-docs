# shouldConnectExternalDomain(completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines whether to connect to a domain from another device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func shouldConnectExternalDomain(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func shouldConnectExternalDomain() async throws
```

```objc
- (void) shouldConnectExternalDomainWithCompletionHandler:(void (^)(NSError *connectionError)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderexternalvolumehandling/shouldconnectexternaldomain(completionhandler:))*