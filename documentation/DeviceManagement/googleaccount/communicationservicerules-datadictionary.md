# GoogleAccount.CommunicationServiceRules

**Framework**: Device Management  
**Kind**: dictionary

The communication service handler rules for this account.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GoogleAccount.CommunicationServiceRules
```

#### Discussion

The rules contain only a `DefaultServiceHandlers` key; its value is a dictionary which contains an `AudioCall` key whose value is a string containing the bundle identifier for the default application that handles audio calls to contacts from this account.

## Topics

### Profiles
- [object GoogleAccount.CommunicationServiceRules.DefaultServiceHandlers](googleaccount/communicationservicerules-data.dictionary/defaultservicehandlers-data.dictionary.md)
  A dictionary of default service handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/googleaccount/communicationservicerules-data.dictionary)*