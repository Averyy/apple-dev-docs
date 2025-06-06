# callCommunications

**Framework**: SMS and Call Reporting  
**Kind**: property

The calls the user selected to report.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var callCommunications: [ILCallCommunication] { get }
```

#### Discussion

The system sorts calls by the date received.

Currently, the user has no way to select multiple calls, so the array should only contain one call. However, in order to future-proof your app, always assume the property might contain more than one call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilcallclassificationrequest/callcommunications)*