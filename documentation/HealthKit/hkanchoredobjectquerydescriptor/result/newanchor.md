# newAnchor

**Framework**: HealthKit  
**Kind**: property

A value corresponding to the last sample that the anchor query has returned.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
let newAnchor: HKQueryAnchor
```

#### Discussion

Subsequent anchor object queries can use this anchor to receive only the samples saved and objects deleted after this query completed.

## See Also

- [let addedSamples: [Sample]](hkanchoredobjectquerydescriptor/result/addedsamples.md)
  An array containing the matching samples added to the HealthKit store.
- [let deletedObjects: [HKDeletedObject]](hkanchoredobjectquerydescriptor/result/deletedobjects.md)
  An array of objects deleted from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/result/newanchor)*