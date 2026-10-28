# excludedZoneIDs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A specific set of zone IDs to exclude from this scope.

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
@property (copy, readonly) NSSet<CKRecordZoneID *> * excludedZoneIDs;
```

## Discussion

If you know that you don’t want to fetch changes for a particular set of zones, you can set those zones here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefetchchangesscope/excludedzoneids)*