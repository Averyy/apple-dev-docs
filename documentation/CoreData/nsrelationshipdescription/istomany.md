# isToMany

**Framework**: Core Data  
**Kind**: property

Returns a Boolean value that indicates whether the relationship can contain many managed objects.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isToMany: Bool { get }
```

#### Discussion

If [`maxCount`](nsrelationshipdescription/maxcount.md) is equal to `1`, implying a to-one relationship, this property returns [`false`](https://developer.apple.com/documentation/Swift/false); otherwise, it returns [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var minCount: Int](nsrelationshipdescription/mincount.md)
  The minimum number of managed objects the relationship can reference.
- [var maxCount: Int](nsrelationshipdescription/maxcount.md)
  The maximum number of managed objects the relationship can reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/istomany)*