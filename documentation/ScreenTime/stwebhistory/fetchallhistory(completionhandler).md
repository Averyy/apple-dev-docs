# fetchAllHistory(completionHandler:)

**Framework**: Screen Time  
**Kind**: method  
**Role**: Instance Method

Fetches all web history associated with the bundle identifier and profile identifier you specified during initialization.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+

## Declaration

```swift
func fetchAllHistory(completionHandler: @escaping @Sendable (Set<URL>?, (any Error)?) -> Void)
```

```swift
func fetchAllHistory() async throws -> Set<URL>
```

```objc
- (void) fetchAllHistoryWithCompletionHandler:(void (^)(NSSet<NSURL *> *urls, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory/fetchallhistory(completionhandler:))*