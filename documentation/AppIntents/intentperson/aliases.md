# aliases

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

Other secondary `Handle`s used to contact this `IntentPerson`, if any

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
var aliases: [IntentPerson.Handle]
```

## See Also

### Getting identifying information
- [var handle: IntentPerson.Handle?](./handle-swift.property.md)
  The primary `Handle` used to contact this `IntentPerson`
- [var isMe: Bool](./isme.md)
  Whether this `IntentPerson` represents the owner of the device
- [var image: DisplayRepresentation.Image?](./image.md)
  An image representing this `IntentPerson`
- [IntentPerson.Handle](./handle-swift.struct.md)
  A type that describes a single way to contact a person.
- [IntentPerson.ParameterMode](./parametermode.md)
  The type of interface to show when someone chooses a parameter that contains information about a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/aliases)*