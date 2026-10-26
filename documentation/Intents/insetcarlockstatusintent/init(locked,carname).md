# init(locked:carName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes an intent to set the lock status of the named car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- watchOS 3.2+

## Declaration

```swift
@nonobjc
convenience init(locked: Bool?, carName: INSpeakableString?)
```

#### Return Value

A newly initialized `INSetCarLockStatusIntent` object.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, Siri creates instances when the user asks it to lock or unlock the car. However, you can use this method during testing to create intent objects to validate your intent-handling code paths.

## Parameters

- `locked`: A Boolean value that indicates whether the car should be locked ([`true`](../../Swift/true.md)) or unlocked ([`false`](../../Swift/false.md)).
- `carName`: A name that identifies the user’s car. If `nil`, the intent is instantiated with a [`carName`](./carname.md) property containing the string `myCar`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintent/init(locked:carname:))*