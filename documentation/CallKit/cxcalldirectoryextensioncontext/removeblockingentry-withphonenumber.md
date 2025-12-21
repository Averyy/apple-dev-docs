# removeBlockingEntry(withPhoneNumber:)

**Framework**: CallKit  
**Kind**: method

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

#### Discussion

If [`isIncremental`](cxcalldirectoryextensioncontext/isincremental.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the request provides incremental entries and may use this method to remove previously added blocking entries. This method removes all blocking entries that contain the specified phone number, even if multiple blocking entries with different labels are present for a single phone number.

Don’t call this method if [`isIncremental`](cxcalldirectoryextensioncontext/isincremental.md) is [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `phoneNumber`: The phone number to remove.

## See Also

- [func removeAllBlockingEntries()](cxcalldirectoryextensioncontext/removeallblockingentries.md)
  Removes all stored blocking entries.
- [func removeAllIdentificationEntries()](cxcalldirectoryextensioncontext/removeallidentificationentries.md)
  Removes all stored identification entries.
- [func removeIdentificationEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](cxcalldirectoryextensioncontext/removeidentificationentry(withphonenumber:).md)
  Removes an identification entry that contains the specified phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/removeblockingentry(withphonenumber:))*