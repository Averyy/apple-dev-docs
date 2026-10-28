# resolveAffinityType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the affinity type to which the media item is updated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveAffinityType(for intent: INUpdateMediaAffinityIntent, with completion: @escaping @Sendable (INMediaAffinityTypeResolutionResult) -> Void)
```

```swift
optional func resolveAffinityType(for intent: INUpdateMediaAffinityIntent) async -> INMediaAffinityTypeResolutionResult
```

```objc
- (void) resolveAffinityTypeForUpdateMediaAffinity:(INUpdateMediaAffinityIntent *) intent withCompletion:(void (^)(INMediaAffinityTypeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the affinity type to which the media item is updated. Always strive toward a successful resolution to the specific media items, but feel free to ask for confirmation of the selected media items if there’s some uncertainty about the media items chosen.

If you find multiple media items matching the same name, consider asking the user to disambiguate from among the most likely candidates.

> **Note**:  Don’t ask users for confirmation or disambiguation too often, as users may become frustrated and exit Siri.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For asuccessful resolution, create a resolution object with the affinity to update to.

## See Also

### Resolving Details of the Intent
- [func resolveMediaItems(for: INUpdateMediaAffinityIntent, with: ([INUpdateMediaAffinityMediaItemResolutionResult]) -> Void)](./resolvemediaitems%28for,with%29.md)
  Resolves the media items for which the user’s preferences are updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintenthandling/resolveaffinitytype(for:with:))*