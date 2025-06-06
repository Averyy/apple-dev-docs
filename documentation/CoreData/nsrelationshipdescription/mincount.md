# minCount

**Framework**: Core Data  
**Kind**: property

The minimum number of managed objects the relationship can reference.

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
var minCount: Int { get set }
```

#### Discussion

If you declare a relationship attribute as optional when defining your entities, the framework only enforces [`minCount`](nsrelationshipdescription/mincount.md) and [`maxCount`](nsrelationshipdescription/maxcount.md) when that attribute is not `nil`.

The default value is `0`.

## See Also

- [var isToMany: Bool](nsrelationshipdescription/istomany.md)
  Returns a Boolean value that indicates whether the relationship can contain many managed objects.
- [var maxCount: Int](nsrelationshipdescription/maxcount.md)
  The maximum number of managed objects the relationship can reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/mincount)*