# addBlockingEntry(withNextSequentialPhoneNumber:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addBlockingEntryWithNextSequentialPhoneNumber:(CXCallDirectoryPhoneNumber) phoneNumber;
```

## Mentions

- [Identifying and blocking calls](../identifying-and-blocking-calls.md)

## Discussion

When a phone number is blocked, the system telephony provider will disallow incoming calls from that phone number without displaying them to the user.

Call this method on the instance of [`CXCallDirectoryExtensionContext`](../cxcalldirectoryextensioncontext.md) passed as an argument to the block parameter of the  [`CXCallDirectoryProvider`](../cxcalldirectoryprovider.md) instance method [`beginRequest(with:)`](../cxcalldirectoryprovider/beginrequest%28with%29.md).

## Parameters

- `phoneNumber`: The phone number to be blocked.

## See Also

### Adding Entries
- [func addIdentificationEntry(withNextSequentialPhoneNumber: CXCallDirectoryPhoneNumber, label: String)](./addidentificationentry%28withnextsequentialphonenumber,label%29.md)
  Adds an identification entry with the specified phone number and label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/addblockingentry(withnextsequentialphonenumber:))*