# checkPendingGameActivityExistence(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Checks whether there is a pending activity to handle for the current game.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func checkPendingGameActivityExistence(completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
class var hasPendingGameActivities: Bool { get async }
```

```objc
+ (void) checkPendingGameActivityExistenceWithCompletionHandler:(void (^)(BOOL )) completionHandler;
```

## Discussion

You can call this method before you initialize Game Center to avoid activating the system banner or welcome experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/checkpendinggameactivityexistence(completionhandler:))*