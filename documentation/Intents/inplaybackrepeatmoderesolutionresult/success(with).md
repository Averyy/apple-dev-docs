# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves successfully matching the specified parameter.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func success(with resolvedPlaybackRepeatMode: INPlaybackRepeatMode) -> Self
```

```objc
+ (instancetype) successWithResolvedPlaybackRepeatMode:(INPlaybackRepeatMode) resolvedPlaybackRepeatMode;
```

#### Return Value

A new [`INPlaybackRepeatModeResolutionResult`](../inplaybackrepeatmoderesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to change the plaback repeat mode for a media item.

## Parameters

- `resolvedPlaybackRepeatMode`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func confirmationRequired(with: INPlaybackRepeatMode) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaybackrepeatmoderesolutionresult/success(with:))*