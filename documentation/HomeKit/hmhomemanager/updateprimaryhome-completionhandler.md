# updatePrimaryHome(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the primary home of this home manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func updatePrimaryHome(_ home: HMHome) async throws
```

## Parameters

- `home`: The new primary home. Must be a home managed by this home manager.
- `completion`: The block executed after the request is processed.

## See Also

- [var primaryHome: HMHome?](hmhomemanager/primaryhome.md)
  The primary home managed by this home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/updateprimaryhome(_:completionhandler:))*