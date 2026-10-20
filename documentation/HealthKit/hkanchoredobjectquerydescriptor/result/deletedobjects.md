# deletedObjects

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

An array of objects deleted from the HealthKit store.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
let deletedObjects: [HKDeletedObject]
```

## See Also

### Accessing the Results
- [let addedSamples: [Sample]](./addedsamples.md)
  An array containing the matching samples added to the HealthKit store.
- [let newAnchor: HKQueryAnchor](./newanchor.md)
  A value corresponding to the last sample that the anchor query has returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/result/deletedobjects)*