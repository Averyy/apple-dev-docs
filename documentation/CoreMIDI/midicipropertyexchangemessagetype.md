# MIDICIPropertyExchangeMessageType

**Framework**: Core MIDI  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum MIDICIPropertyExchangeMessageType
```

```c
enum MIDICIPropertyExchangeMessageType : MIDIUInteger7;
```

## Topics

### Enumeration Cases
- [MIDICIPropertyExchangeMessageType.inquiryGetPropertyData](./midicipropertyexchangemessagetype/inquirygetpropertydata.md)
- [MIDICIPropertyExchangeMessageType.inquiryHasPropertyData_Reserved](./midicipropertyexchangemessagetype/inquiryhaspropertydata_reserved.md)
- [MIDICIPropertyExchangeMessageType.inquiryPropertyExchangeCapabilities](./midicipropertyexchangemessagetype/inquirypropertyexchangecapabilities.md)
- [MIDICIPropertyExchangeMessageType.inquiryReplyToHasPropertyData_Reserved](./midicipropertyexchangemessagetype/inquiryreplytohaspropertydata_reserved.md)
- [MIDICIPropertyExchangeMessageType.inquirySetPropertyData](./midicipropertyexchangemessagetype/inquirysetpropertydata.md)
- [MIDICIPropertyExchangeMessageType.notify](./midicipropertyexchangemessagetype/notify.md)
- [MIDICIPropertyExchangeMessageType.replyToGetProperty](./midicipropertyexchangemessagetype/replytogetproperty.md)
- [MIDICIPropertyExchangeMessageType.replyToPropertyExchangeCapabilities](./midicipropertyexchangemessagetype/replytopropertyexchangecapabilities.md)
- [MIDICIPropertyExchangeMessageType.replyToSetPropertyData](./midicipropertyexchangemessagetype/replytosetpropertydata.md)
- [MIDICIPropertyExchangeMessageType.replyToSubscription](./midicipropertyexchangemessagetype/replytosubscription.md)
- [MIDICIPropertyExchangeMessageType.subscription](./midicipropertyexchangemessagetype/subscription.md)
### Initializers
- [init?(rawValue: MIDIUInteger7)](./midicipropertyexchangemessagetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [var kMIDIInvalidUniqueID: MIDIUniqueID](./kmidiinvaliduniqueid.md)
  An invalid identifier.
- [struct MIDICICategoryOptions](./midicicategoryoptions.md)
- [enum MIDICIDeviceType](./midicidevicetype.md)
- [enum MIDICIManagementMessageType](./midicimanagementmessagetype.md)
- [enum MIDICIProcessInquiryMessageType](./midiciprocessinquirymessagetype.md)
- [enum MIDICIProfileMessageType](./midiciprofilemessagetype.md)
- [enum MIDICIProfileType](./midiciprofiletype.md)
- [enum MIDINetworkConnectionPolicy](./midinetworkconnectionpolicy.md)
- [enum MIDINoteAttribute](./midinoteattribute.md)
- [struct MIDIPerNoteManagementOptions](./midipernotemanagementoptions.md)
- [struct MIDIProgramChangeOptions](./midiprogramchangeoptions.md)
- [enum MIDIUMPCIObjectBackingType](./midiumpciobjectbackingtype.md)
- [enum MIDIUMPFunctionBlockDirection](./midiumpfunctionblockdirection.md)
- [enum MIDIUMPFunctionBlockMIDI1Info](./midiumpfunctionblockmidi1info.md)
- [enum MIDIUMPFunctionBlockUIHint](./midiumpfunctionblockuihint.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicipropertyexchangemessagetype)*