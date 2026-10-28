# addIdentificationEntry(withNextSequentialPhoneNumber:label:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Adds an identification entry with the specified phone number and label.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
func addIdentificationEntry(withNextSequentialPhoneNumber phoneNumber: CXCallDirectoryPhoneNumber, label: String)
```

```objc
- (void) addIdentificationEntryWithNextSequentialPhoneNumber:(CXCallDirectoryPhoneNumber) phoneNumber label:(NSString *) label;
```

## Mentions

- [Identifying and blocking calls](../identifying-and-blocking-calls.md)

## Discussion

When a phone number has an identification entry, incoming calls from that phone number will display its associated label to the user.

Call this method on the instance of [`CXCallDirectoryExtensionContext`](../cxcalldirectoryextensioncontext.md) passed as an argument to the block parameter of the  [`CXCallDirectoryProvider`](../cxcalldirectoryprovider.md) instance method [`beginRequest(with:)`](../cxcalldirectoryprovider/beginrequest%28with%29.md).

## Parameters

- `phoneNumber`: The phone number to be identified.
- `label`: The label to identify the phone number.

## See Also

### Adding Entries
- [func addBlockingEntry(withNextSequentialPhoneNumber: CXCallDirectoryPhoneNumber)](./addblockingentry%28withnextsequentialphonenumber%29.md)
  Adds a blocking entry with the specified phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/addidentificationentry(withnextsequentialphonenumber:label:))*