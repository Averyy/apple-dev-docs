# NSQueryGenerationToken

**Framework**: Core Data  
**Kind**: class

A token that indicates which generation of the persistent store is being accessed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class NSQueryGenerationToken
```

## Mentions

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)

#### Overview

When a managed object context is pinned to a specific generation of the app data, a query generation token will be associated with that context.

## Topics

### Identifying Generations of App Data
- [class var current: NSQueryGenerationToken](nsquerygenerationtoken/current.md)
  A token that informs a context to use the current generation.
### Initializers
- [init?(coder: NSCoder)](nsquerygenerationtoken/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class NSConstraintConflict](nsconstraintconflict.md)
  An encapsulation of conflicts that occur during an attempt to save a managed object.
- [class NSMergeConflict](nsmergeconflict.md)
  An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [class NSMergePolicy](nsmergepolicy.md)
  A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsquerygenerationtoken)*