# NSQueryGenerationToken

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSQueryGenerationToken : NSObject
```

## Mentions

- [Accessing data when the store changes](./accessing-data-when-the-store-changes.md)

#### Overview

When a managed object context is pinned to a specific generation of the app data, a query generation token will be associated with that context.

## Topics

### Identifying Generations of App Data
- [class var current: NSQueryGenerationToken](./nsquerygenerationtoken/current.md)
  A token that informs a context to use the current generation.
### Initializers
- [init?(coder: NSCoder)](./nsquerygenerationtoken/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Conflict Management
- [class NSConstraintConflict](./nsconstraintconflict.md)
  An encapsulation of conflicts that occur during an attempt to save a managed object.
- [class NSMergeConflict](./nsmergeconflict.md)
  An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [class NSMergePolicy](./nsmergepolicy.md)
  A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsquerygenerationtoken)*