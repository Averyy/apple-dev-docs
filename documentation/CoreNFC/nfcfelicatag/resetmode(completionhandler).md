# resetMode(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Reset Mode command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func resetMode(completionHandler: @escaping @Sendable (Int, Int, (any Error)?) -> Void)
```

```swift
func resetMode() async throws -> (Int, Int)
```

```objc
- (void) resetModeWithCompletionHandler:(void (^)(NSInteger statusFlag1, NSInteger statusFlag2, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/resetmode(completionhandler:))*