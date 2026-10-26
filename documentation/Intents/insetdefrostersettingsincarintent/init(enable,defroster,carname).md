# init(enable:defroster:carName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified defroster information.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 12.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
convenience init(enable: Bool? = nil, defroster: INCarDefroster = .unknown, carName: INSpeakableString? = nil)
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to change the vehicle’s defroster settings. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `enable`: A Boolean value indicating whether to enable or disable the defroster. Specify [`true`](../../Swift/true.md) to turn the defroster on or [`false`](../../Swift/false.md) to turn it off.
- `defroster`: The defroster to enable or disable.
- `carName`: The name of the car to apply the defroster setting to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintent/init(enable:defroster:carname:))*