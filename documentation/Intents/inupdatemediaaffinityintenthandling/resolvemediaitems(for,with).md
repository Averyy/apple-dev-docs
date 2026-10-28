# resolveMediaItems(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the media items for which the user’s preferences are updated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveMediaItems(for intent: INUpdateMediaAffinityIntent, with completion: @escaping @Sendable ([INUpdateMediaAffinityMediaItemResolutionResult]) -> Void)
```

```swift
optional func resolveMediaItems(for intent: INUpdateMediaAffinityIntent) async -> [INUpdateMediaAffinityMediaItemResolutionResult]
```

```objc
- (void) resolveMediaItemsForUpdateMediaAffinity:(INUpdateMediaAffinityIntent *) intent withCompletion:(void (^)(NSArray<INUpdateMediaAffinityMediaItemResolutionResult *> *resolutionResults)) completion;
```

## Discussion

Implement this method to resolve the media items to update. Always strive toward a successful resolution to the specific media items, but feel free to ask for confirmation of the selected media items if there’s some uncertainty.

If you find multiple media items matching the same name, consider asking the user to disambiguate from among the most likely candidates.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution object with updated preference for the media item.

## See Also

### Resolving Details of the Intent
- [func resolveAffinityType(for: INUpdateMediaAffinityIntent, with: (INMediaAffinityTypeResolutionResult) -> Void)](./resolveaffinitytype%28for,with%29.md)
  Resolves the affinity type to which the media item is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintenthandling/resolvemediaitems(for:with:))*