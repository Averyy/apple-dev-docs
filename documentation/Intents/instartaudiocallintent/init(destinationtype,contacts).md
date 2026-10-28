# init(destinationType:contacts:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an intent with the specified information.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

## Declaration

```swift
init(destinationType: INCallDestinationType, contacts: [INPerson]?)
```

```objc
- (instancetype) initWithDestinationType:(INCallDestinationType) destinationType contacts:(NSArray<INPerson *> *) contacts;
```

## Return Value

An initialized intent or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to place a call to another user. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `destinationType`: The type of call to place.
- `contacts`: An array of [`INPerson`](../inperson.md) objects representing the users to call.

## See Also

### Creating the Intent Object
- [convenience init(contacts: [INPerson]?)](./init%28contacts%29.md)
  Initializes the start audio call intent object with the specified contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintent/init(destinationtype:contacts:))*