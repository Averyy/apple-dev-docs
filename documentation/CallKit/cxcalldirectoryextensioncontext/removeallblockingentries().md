# removeAllBlockingEntries()

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeAllBlockingEntries;
```

#### Discussion

If [`isIncremental`](./isincremental.md) is [`true`](../../Swift/true.md), the request provides incremental entries and may use this method to remove all previously added blocking entries. Don’t call this method if [`isIncremental`](./isincremental.md) is [`false`](../../Swift/false.md).

## See Also

### Removing Entries
- [func removeAllIdentificationEntries()](./removeallidentificationentries%28%29.md)
  Removes all stored identification entries.
- [func removeBlockingEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](./removeblockingentry%28withphonenumber%29.md)
  Removes a blocking entry that contains the specified phone number.
- [func removeIdentificationEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](./removeidentificationentry%28withphonenumber%29.md)
  Removes an identification entry that contains the specified phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/removeallblockingentries())*