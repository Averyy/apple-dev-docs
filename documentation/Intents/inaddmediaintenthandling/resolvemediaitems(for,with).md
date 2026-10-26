# resolveMediaItems(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the media items to add.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveMediaItems(for intent: INAddMediaIntent, with completion: @escaping @Sendable ([INAddMediaMediaItemResolutionResult]) -> Void)
```

```swift
optional func resolveMediaItems(for intent: INAddMediaIntent) async -> [INAddMediaMediaItemResolutionResult]
```

```objc
- (void) resolveMediaItemsForAddMedia:(INAddMediaIntent *) intent withCompletion:(void (^)(NSArray<INAddMediaMediaItemResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

Implement this method to resolve the media items to add. Always strive toward a successful resolution to the specific media items, but feel free to ask for confirmation of the selected media items if there’s some uncertainty about whether you are adding the correct media items.

If you find multiple media items matching the same name, consider asking the user to disambiguate from among the most likely candidates.

> **Note**:  Don’t ask users for confirmation or disambiguation too often, as users may become frustrated and exit Siri.

## Parameters

- `intent`: The intent object that contain details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution.

## See Also

### Resolving Details of the Intent
- [func resolveMediaDestination(for: INAddMediaIntent, with: (INAddMediaMediaDestinationResolutionResult) -> Void)](./resolvemediadestination%28for,with%29.md)
  Resolves the destination for the added media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintenthandling/resolvemediaitems(for:with:))*