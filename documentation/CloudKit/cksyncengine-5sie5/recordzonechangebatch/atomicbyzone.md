# atomicByZone

**Framework**: CloudKit  
**Kind**: property

A Boolean value that determines whether CloudKit modifies records atomically by record zone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
var atomicByZone: Bool
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/swift/true), CloudKit processes record changes atomically by record zone, and if any individual change fails, all other changes in that record’s record zone fail and return an error of type [`CKError.Code.batchRequestFailed`](ckerror/code/batchrequestfailed.md).

The default value is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/recordzonechangebatch/atomicbyzone)*