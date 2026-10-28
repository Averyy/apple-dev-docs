# initWithProfileNumber:profileName:defaultProfile:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the intent object with the specified profile name and index information.

**Availability**:
- iOS 10.2+ - Deprecated in 12.0
- iPadOS 10.2+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.1+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.1+ - Deprecated in 5.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
- (instancetype) initWithProfileNumber:(NSNumber *) profileNumber profileName:(NSString *) profileName defaultProfile:(NSNumber *) defaultProfile;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to restore settings from a profile. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `profileNumber`: An integer number that indicates which profile to use. This value represents the index of the profile in your system. The index can be a soft index inside your vehicle’s electronics systems or it can correspond to physical buttons that the user presses.
- `profileName`: The name of the profile. Specify `nil` when creating a profile based on a numerical index.
- `defaultProfile`: A Boolean value that indicates whether the profile should become the default profile.

## See Also

### Initializing the Intent Object
- [- initWithProfileNumber:profileName:defaultProfile:carName:](./initwithprofilenumber_profilename_defaultprofile_carname_.md)
  Initializes the intent object with the specified profile name and index information.
- [- initWithProfileNumber:profileLabel:defaultProfile:](./initwithprofilenumber_profilelabel_defaultprofile_.md)
  Initializes the intent object with the specified profile name and index information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent/initwithprofilenumber:profilename:defaultprofile:)*