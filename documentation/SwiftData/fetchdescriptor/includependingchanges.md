# includePendingChanges

**Framework**: SwiftData  
**Kind**: property

A Boolean value that indicates whether, when the fetch runs, it matches against currently unsaved changes in the model context.

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
var includePendingChanges: Bool
```

#### Discussion

Set this property’s value to `false` to ignore any unsaved changes in the model context and match against a model’s persisted state instead.

The default value is `true`.

## See Also

- [var predicate: Predicate<T>?](fetchdescriptor/predicate.md)
  The logical condition that determines whether the fetch includes a specific model in its results.
- [var sortBy: [SortDescriptor<T>]](fetchdescriptor/sortby.md)
  The sort descriptors that tell the fetch how to order its results.
- [var fetchLimit: Int?](fetchdescriptor/fetchlimit.md)
  The maximum number of models the fetch can return.
- [var fetchOffset: Int?](fetchdescriptor/fetchoffset.md)
  The offset of the first matching model to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchdescriptor/includependingchanges)*