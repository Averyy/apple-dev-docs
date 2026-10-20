# removeBlockingEntry(withPhoneNumber:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Removes a blocking entry that contains the specified phone number.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeBlockingEntry(withPhoneNumber phoneNumber: CXCallDirectoryPhoneNumber)
```

```objc
- (void) removeBlockingEntryWithPhoneNumber:(CXCallDirectoryPhoneNumber) phoneNumber;
```

#### Discussion

If [`isIncremental`](./isincremental.md) is [`true`](../../Swift/true.md), the request provides incremental entries and may use this method to remove previously added blocking entries. This method removes all blocking entries that contain the specified phone number, even if multiple blocking entries with different labels are present for a single phone number.

Don’t call this method if [`isIncremental`](./isincremental.md) is [`false`](../../Swift/false.md).

## Parameters

- `phoneNumber`: The phone number to remove.

## See Also

### Removing Entries
- [func removeAllBlockingEntries()](./removeallblockingentries%28%29.md)
  Removes all stored blocking entries.
- [func removeAllIdentificationEntries()](./removeallidentificationentries%28%29.md)
  Removes all stored identification entries.
- [func removeIdentificationEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](./removeidentificationentry%28withphonenumber%29.md)
  Removes an identification entry that contains the specified phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/removeblockingentry(withphonenumber:))*