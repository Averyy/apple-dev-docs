# updatePrimaryHome(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the primary home of this home manager.

**Availability**:
- iOS 8.0+ - Deprecated in 16.1
- iPadOS 8.0+ - Deprecated in 16.1
- Mac Catalyst 13.1+ - Deprecated in 16.1
- tvOS 10.0+ - Deprecated in 16.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 9.1

> **Deprecated**: This method is no longer supported.

## Declaration

```swift
func updatePrimaryHome(_ home: HMHome, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updatePrimaryHome(_ home: HMHome) async throws
```

```objc
- (void) updatePrimaryHome:(HMHome *) home completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `home`: The new primary home. Must be a home managed by this home manager.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Deprecated
- [var primaryHome: HMHome?](./primaryhome.md)
  The primary home managed by this home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/updateprimaryhome(_:completionhandler:))*