# initWithProfileNumber:profileLabel:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the intent object with the specified profile name information.

**Availability**:
- iOS 10.0+ - Deprecated in 10.2
- iPadOS 10.0+ - Deprecated in 10.2
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 10.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
- (instancetype) initWithProfileNumber:(NSNumber *) profileNumber profileLabel:(NSString *) profileLabel;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to save the current settings. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `profileNumber`: An integer number to use when saving the profile. This value represents the index of the profile in your system. The index can be a soft index inside your vehicle’s electronics systems or it can correspond to physical buttons that the user presses.
- `profileLabel`: The name of the profile.

## See Also

### Initializing the Intent Object
- [- initWithProfileNumber:profileName:](./initwithprofilenumber_profilename_.md)
  Initializes the intent object with the specified profile name information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintent/initwithprofilenumber:profilelabel:)*