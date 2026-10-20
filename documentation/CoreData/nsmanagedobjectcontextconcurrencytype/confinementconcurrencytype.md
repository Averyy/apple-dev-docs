# NSManagedObjectContextConcurrencyType.confinementConcurrencyType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

Specifies that the context will use the thread confinement pattern.

**Availability**:
- iOS 3.0+ - Deprecated in 9.0
- iPadOS 3.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.11
- tvOS - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use another NSManagedObjectContextConcurrencyType

## Declaration

```swift
case confinementConcurrencyType
```

```c
NSConfinementConcurrencyType
```

## See Also

### Concurrency Types
- [NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType](./privatequeueconcurrencytype.md)
  Specifies that the context will be associated with a private dispatch queue.
- [NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType](./mainqueueconcurrencytype.md)
  Specifies that the context will be associated with the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)*