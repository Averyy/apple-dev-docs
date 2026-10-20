# isToMany

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the relationship can contain many managed objects.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isToMany: Bool { get }
```

```objc
@property (readonly, getter=isToMany) BOOL toMany;
```

#### Discussion

If [`maxCount`](./maxcount.md) is equal to `1`, implying a to-one relationship, this property returns [`false`](../../Swift/false.md); otherwise, it returns [`true`](../../Swift/true.md).

## See Also

### Configuring Cardinality
- [var minCount: Int](./mincount.md)
  The minimum number of managed objects the relationship can reference.
- [var maxCount: Int](./maxcount.md)
  The maximum number of managed objects the relationship can reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/istomany)*