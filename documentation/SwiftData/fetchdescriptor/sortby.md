# sortBy

**Framework**: SwiftData  
**Kind**: property

The sort descriptors that tell the fetch how to order its results.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
var sortBy: [SortDescriptor<T>]
```

#### Discussion

Use this property to specify how to arrange the collection of models that a fetch returns. For example, if your app defines a `Person` model, you may want to sort by the `surname` attribute, then by the `firstName` attribute. The fetch applies the sort descriptors in the same order as they appear in the array.

The default value is the array you specify when calling [`init(predicate:sortBy:)`](fetchdescriptor/init(predicate:sortby:).md).

## See Also

- [var predicate: Predicate<T>?](fetchdescriptor/predicate.md)
  The logical condition that determines whether the fetch includes a specific model in its results.
- [var fetchLimit: Int?](fetchdescriptor/fetchlimit.md)
  The maximum number of models the fetch can return.
- [var fetchOffset: Int?](fetchdescriptor/fetchoffset.md)
  The offset of the first matching model to fetch.
- [var includePendingChanges: Bool](fetchdescriptor/includependingchanges.md)
  A Boolean value that indicates whether, when the fetch runs, it matches against currently unsaved changes in the model context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchdescriptor/sortby)*