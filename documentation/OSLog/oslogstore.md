# OSLogStore

**Framework**: OSLog  
**Kind**: class

A set of entries from the unified logging system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class OSLogStore
```

#### Overview

Instances of this class represent a fixed range of entries and may be backed by a `logarchive` or your Mac’s local store.

In Swift, Use the [`getEntries(with:at:matching:)`](oslogstore/getentries(with:at:matching:).md) function to retrieve a filtered array of log entries.

In Objective-C, use instances of this class to create [`OSLogEnumerator`](oslogenumerator.md) objects. One store can support multiple `OSLogEnumerator` instances concurrently.

## Topics

### Creating Log Stores
- [convenience init(url: URL) throws](oslogstore/init(url:).md)
  Creates a log store based on a log archive.
- [class func local() throws -> Self](oslogstore/local.md)
  Creates a log store representing the Mac’s local store.
### Accessing Position
- [func position(date: Date) -> OSLogPosition](oslogstore/position(date:).md)
  Returns a position representing the time specified.
- [func position(timeIntervalSinceEnd: TimeInterval) -> OSLogPosition](oslogstore/position(timeintervalsinceend:).md)
  Returns a position representing time since the end of the time range that the entries span.
- [func position(timeIntervalSinceLatestBoot: TimeInterval) -> OSLogPosition](oslogstore/position(timeintervalsincelatestboot:).md)
  Returns a position representing time since the last boot in the series of entries.
### Accessing Entries
- [func getEntries(with: OSLogEnumerator.Options, at: OSLogPosition?, matching: NSPredicate?) throws -> AnySequence<OSLogEntry>](oslogstore/getentries(with:at:matching:).md)
  Returns a sequence of log entries filtered by the parameters passed in.
### Initializers
- [init()](oslogstore/init.md)
- [convenience init(scope: OSLogStore.Scope) throws](oslogstore/init(scope:).md)
### Enumerations
- [OSLogStore.Scope](oslogstore/scope.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class OSLogEnumerator](oslogenumerator.md)
  An enumerator that can access and list log entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore)*