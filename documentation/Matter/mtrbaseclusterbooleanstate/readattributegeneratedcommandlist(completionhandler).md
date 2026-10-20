# readAttributeGeneratedCommandList(completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use readAttributeGeneratedCommandListWithCompletion:

## Declaration

```swift
func readAttributeGeneratedCommandList(completionHandler: @escaping @Sendable ([Any]?, (any Error)?) -> Void)
```

```swift
func readAttributeGeneratedCommandList() async throws -> [Any]
```

```objc
- (void) readAttributeGeneratedCommandListWithCompletionHandler:(void (^)(NSArray *value, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbooleanstate/readattributegeneratedcommandlist(completionhandler:))*