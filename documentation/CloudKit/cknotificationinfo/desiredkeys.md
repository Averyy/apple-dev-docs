# desiredKeys

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The names of fields to include in the push notification’s payload.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
@property (copy, nullable) NSArray<NSString *> * desiredKeys;
```

#### Discussion

This property contains an array of strings, each of which corresponds to the name of a field in the record that triggers the notification. When the system receives a notification, it includes the keys, and their corresponding values. You can request a maximum of three keys.

For the keys you specify, the allowable types are [`NSString`](../../Foundation/nsstring.md), [`NSNumber`](../../Foundation/nsnumber.md), [`CLLocation`](../../CoreLocation/cllocation.md), [`NSDate`](../../Foundation/nsdate.md), and [`CKRecord.Reference`](../ckrecord/reference.md). You can’t specify keys with values that contain other data types. CloudKit may truncate strings that are more than 100 characters when it adds them to the notification’s payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/desiredkeys)*