# requestSpecificationVersion(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Request Specification Version command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func requestSpecificationVersion(completionHandler: @escaping @Sendable (Int, Int, Data, Data, (any Error)?) -> Void)
```

```swift
func requestSpecificationVersion() async throws -> (Int, Int, Data, Data)
```

```objc
- (void) requestSpecificationVersionWithCompletionHandler:(void (^)(NSInteger statusFlag1, NSInteger statusFlag2, NSData *basicVersion, NSData *optionVersion, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/requestspecificationversion(completionhandler:))*