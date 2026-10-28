# resolveMediaDestination(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the destination for the added media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveMediaDestination(for intent: INAddMediaIntent, with completion: @escaping @Sendable (INAddMediaMediaDestinationResolutionResult) -> Void)
```

```swift
optional func resolveMediaDestination(for intent: INAddMediaIntent) async -> INAddMediaMediaDestinationResolutionResult
```

```objc
- (void) resolveMediaDestinationForAddMedia:(INAddMediaIntent *) intent withCompletion:(void (^)(INAddMediaMediaDestinationResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify the destination for the media your app adds.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution object with the destination for the media.

## See Also

### Resolving Details of the Intent
- [func resolveMediaItems(for: INAddMediaIntent, with: ([INAddMediaMediaItemResolutionResult]) -> Void)](./resolvemediaitems%28for,with%29.md)
  Resolves the media items to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintenthandling/resolvemediadestination(for:with:))*