# resolveAttribute(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the attribute to apply to the messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func resolveAttribute(for intent: INSetMessageAttributeIntent, with completion: @escaping @Sendable (INMessageAttributeResolutionResult) -> Void)
```

```swift
optional func resolveAttribute(for intent: INSetMessageAttributeIntent) async -> INMessageAttributeResolutionResult
```

```objc
- (void) resolveAttributeForSetMessageAttribute:(INSetMessageAttributeIntent *) intent withCompletion:(void (^)(INMessageAttributeResolutionResult *resolutionResult)) completion;
```

#### Discussion

This method resolves the attribute to apply to the messages.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For successful resolutions, create a resolution object that contains the [`INMessageAttribute`](../inmessageattribute.md) value that you plan to apply to the messages. If your app does not support modifications to the specified attribute, return a successful resolution and use your response object to report the failure when handling the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintenthandling/resolveattribute(for:with:))*