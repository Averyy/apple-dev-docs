# addBlockingEntry(withNextSequentialPhoneNumber:)

**Framework**: CallKit  
**Kind**: method

Adds a blocking entry with the specified phone number.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
func addBlockingEntry(withNextSequentialPhoneNumber phoneNumber: CXCallDirectoryPhoneNumber)
```

## Mentions

- [Identifying and blocking calls](identifying-and-blocking-calls.md)

#### Discussion

When a phone number is blocked, the system telephony provider will disallow incoming calls from that phone number without displaying them to the user.

Call this method on the instance of [`CXCallDirectoryExtensionContext`](cxcalldirectoryextensioncontext.md) passed as an argument to the block parameter of the  [`CXCallDirectoryProvider`](cxcalldirectoryprovider.md) instance method [`beginRequest(with:)`](cxcalldirectoryprovider/beginrequest(with:).md).

## Parameters

- `phoneNumber`: The phone number to be blocked.

## See Also

- [func addIdentificationEntry(withNextSequentialPhoneNumber: CXCallDirectoryPhoneNumber, label: String)](cxcalldirectoryextensioncontext/addidentificationentry(withnextsequentialphonenumber:label:).md)
  Adds an identification entry with the specified phone number and label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/addblockingentry(withnextsequentialphonenumber:))*