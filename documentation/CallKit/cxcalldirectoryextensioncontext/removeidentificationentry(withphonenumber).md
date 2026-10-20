# removeIdentificationEntry(withPhoneNumber:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Removes an identification entry that contains the specified phone number.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeIdentificationEntry(withPhoneNumber phoneNumber: CXCallDirectoryPhoneNumber)
```

```objc
- (void) removeIdentificationEntryWithPhoneNumber:(CXCallDirectoryPhoneNumber) phoneNumber;
```

#### Discussion

If [`isIncremental`](./isincremental.md) is [`true`](../../Swift/true.md), the request provides incremental entries and may use this method to remove previously added identification entries. This method removes all identification entries that contain the specified phone number, even if multiple identification entries with different labels are present for a single phone number.

Don’t call this method if [`isIncremental`](./isincremental.md) is [`false`](../../Swift/false.md).

## Parameters

- `phoneNumber`: The phone number to remove.

## See Also

### Removing Entries
- [func removeAllBlockingEntries()](./removeallblockingentries%28%29.md)
  Removes all stored blocking entries.
- [func removeAllIdentificationEntries()](./removeallidentificationentries%28%29.md)
  Removes all stored identification entries.
- [func removeBlockingEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](./removeblockingentry%28withphonenumber%29.md)
  Removes a blocking entry that contains the specified phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/removeidentificationentry(withphonenumber:))*