# removeHome(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes a home from this home manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeHome(_ home: HMHome, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeHome(_ home: HMHome) async throws
```

```objc
- (void) removeHome:(HMHome *) home completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

This method returns an error if the specified home is not managed by the home manager.

## Parameters

- `home`: The home to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Adding and removing homes
- [func addHome(withName: String, completionHandler: (HMHome?, (any Error)?) -> Void)](./addhome%28withname,completionhandler%29.md)
  Adds a new home to this home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/removehome(_:completionhandler:))*