# hasActiveChallenges(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Indicates if this definition has active challenges associated with it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func hasActiveChallenges(completionHandler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
var hasActiveChallenges: Bool { get async throws }
```

```objc
- (void) hasActiveChallengesWithCompletionHandler:(void (^)(BOOL hasActiveChallenges, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengedefinition/hasactivechallenges(completionhandler:))*