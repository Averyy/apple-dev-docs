# NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

Specifies that the context will be associated with the main queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case mainQueueConcurrencyType
```

```c
NSMainQueueConcurrencyType
```

## Mentions

- [Using Core Data in the background](../using-core-data-in-the-background.md)

## See Also

### Concurrency Types
- [NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType](./privatequeueconcurrencytype.md)
  Specifies that the context will be associated with a private dispatch queue.
- [NSManagedObjectContextConcurrencyType.confinementConcurrencyType](./confinementconcurrencytype.md)
  Specifies that the context will use the thread confinement pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype)*