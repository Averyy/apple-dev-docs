# init(visualCodeType:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with information about the requested type of code.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(visualCodeType: INVisualCodeType)
```

```objc
- (instancetype) initWithVisualCodeType:(INVisualCodeType) visualCodeType;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks for a visual code from your app. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `visualCodeType`: The type of visual code that the user requested. For a list of possible values, see [`INVisualCodeType`](../invisualcodetype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintent/init(visualcodetype:))*