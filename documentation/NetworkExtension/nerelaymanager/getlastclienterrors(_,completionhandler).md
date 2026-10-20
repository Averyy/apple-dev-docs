# getLastClientErrors(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func getLastClientErrors(_ seconds: TimeInterval, completionHandler: @escaping @Sendable ([any Error]?) -> Void)
```

```swift
func lastClientErrors(_ seconds: TimeInterval) async -> [any Error]?
```

```objc
- (void) getLastClientErrors:(NSTimeInterval) seconds completionHandler:(void (^)(NSArray<NSError *> *errors)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/getlastclienterrors(_:completionhandler:))*