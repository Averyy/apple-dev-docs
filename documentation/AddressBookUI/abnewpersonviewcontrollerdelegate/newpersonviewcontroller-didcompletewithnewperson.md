# newPersonViewController(_:didCompleteWithNewPerson:)

**Framework**: Address Book UI  
**Kind**: method  
**Required**: Yes

Sent when the user taps Save or Cancel. If the user tapped Save, the current address book has been saved to the Address Book database.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func newPersonViewController(_ newPersonView: ABNewPersonViewController, didCompleteWithNewPerson person: ABRecord?)
```

#### Discussion

If the user tapped Save, pending changes in the current address book (`ABAddressBook`) have been saved by the time this message is sent to the receiver.

The receiver must dismiss `newPersonViewController`.

## Parameters

- `person`: On Cancel,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontrollerdelegate/newpersonviewcontroller(_:didcompletewithnewperson:))*