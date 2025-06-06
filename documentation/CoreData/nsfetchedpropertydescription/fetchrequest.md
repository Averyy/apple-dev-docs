# fetchRequest

**Framework**: Core Data  
**Kind**: property

The fetch request of the receiver.

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
var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get set }
```

#### Discussion

Setting the fetch request raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [Predicate Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedpropertydescription/fetchrequest)*