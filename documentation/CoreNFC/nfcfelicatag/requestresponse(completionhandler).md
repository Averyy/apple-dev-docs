# requestResponse(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Request Response command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func requestResponse(completionHandler: @escaping @Sendable (Int, (any Error)?) -> Void)
```

```swift
func requestResponse() async throws -> Int
```

```objc
- (void) requestResponseWithCompletionHandler:(void (^)(NSInteger mode, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/requestresponse(completionhandler:))*