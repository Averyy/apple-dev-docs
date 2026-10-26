# init(call:dateCreated:recipient:callCapabilities:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(call callType: INCallRecordType, dateCreated: INDateComponentsRange?, recipient: INPerson?, callCapabilities: INCallCapabilityOptions = [])
```

```objc
- (instancetype) initWithCallType:(INCallRecordType) callType dateCreated:(INDateComponentsRange *) dateCreated recipient:(INPerson *) recipient callCapabilities:(INCallCapabilityOptions) callCapabilities;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/init(call:datecreated:recipient:callcapabilities:))*