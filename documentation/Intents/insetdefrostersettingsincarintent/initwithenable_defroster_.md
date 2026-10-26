# initWithEnable:defroster:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the intent object with the specified defroster information.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 5.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
- (instancetype) initWithEnable:(NSNumber *) enable defroster:(INCarDefroster) defroster;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to change the vehicle’s defroster settings. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `enable`: A number object containing a Boolean value indicating whether to enable or disable the defroster. Specify [`true`](../../Swift/true.md) to turn the defroster on or [`false`](../../Swift/false.md) to turn it off.
- `defroster`: The defroster to enable or disable.

## See Also

### Initializing the Intent Object
- [- initWithEnable:defroster:carName:](./initwithenable_defroster_carname_.md)
  Initializes the intent object with the specified defroster information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintent/initwithenable:defroster:)*