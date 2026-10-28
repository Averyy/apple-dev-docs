# atomicByZone

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether CloudKit modifies records atomically by record zone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (assign) BOOL atomicByZone;
```

## Discussion

When [`true`](../../Swift/true.md), CloudKit processes record changes atomically by record zone, and if any individual change fails, all other changes in that record’s record zone fail and return an error of type [`CKError.Code.batchRequestFailed`](../ckerror/code/batchrequestfailed.md).

The default value is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginerecordzonechangebatch/atomicbyzone)*