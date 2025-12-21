# removeAllBlockingEntries()

**Framework**: CallKit  
**Kind**: method

Removes all stored blocking entries.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeAllBlockingEntries()
```

#### Discussion

If [`isIncremental`](cxcalldirectoryextensioncontext/isincremental.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the request provides incremental entries and may use this method to remove all previously added blocking entries. Don’t call this method if [`isIncremental`](cxcalldirectoryextensioncontext/isincremental.md) is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func removeAllIdentificationEntries()](cxcalldirectoryextensioncontext/removeallidentificationentries.md)
  Removes all stored identification entries.
- [func removeBlockingEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](cxcalldirectoryextensioncontext/removeblockingentry(withphonenumber:).md)
  Removes a blocking entry that contains the specified phone number.
- [func removeIdentificationEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](cxcalldirectoryextensioncontext/removeidentificationentry(withphonenumber:).md)
  Removes an identification entry that contains the specified phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/removeallblockingentries())*