# OSLogStore

**Framework**: OSLog  
**Kind**: class  
**Role**: Class

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

```objc
@interface OSLogStore : NSObject
```

#### Overview

Instances of this class represent a fixed range of entries and may be backed by a `logarchive` or your Mac’s local store.

In Swift, Use the [`getEntries(with:at:matching:)`](./oslogstore/getentries%28with,at,matching%29.md) function to retrieve a filtered array of log entries.

In Objective-C, use instances of this class to create [`OSLogEnumerator`](./oslogenumerator.md) objects. One store can support multiple `OSLogEnumerator` instances concurrently.

## Topics

### Creating Log Stores
- [convenience init(url: URL) throws](./oslogstore/init%28url%29-5v3w7.md)
  Creates a log store based on a log archive.
- [class func local() throws -> Self](./oslogstore/local%28%29.md)
  Creates a log store representing the Mac’s local store.
### Accessing Position
- [func position(date: Date) -> OSLogPosition](./oslogstore/position%28date%29.md)
  Returns a position representing the time specified.
- [func position(timeIntervalSinceEnd: TimeInterval) -> OSLogPosition](./oslogstore/position%28timeintervalsinceend%29.md)
  Returns a position representing time since the end of the time range that the entries span.
- [func position(timeIntervalSinceLatestBoot: TimeInterval) -> OSLogPosition](./oslogstore/position%28timeintervalsincelatestboot%29.md)
  Returns a position representing time since the last boot in the series of entries.
### Accessing Entries
- [func getEntries(with: OSLogEnumerator.Options, at: OSLogPosition?, matching: NSPredicate?) throws -> AnySequence<OSLogEntry>](./oslogstore/getentries%28with,at,matching%29.md)
  Returns a sequence of log entries filtered by the parameters passed in.
- [- entriesEnumeratorAndReturnError:](./oslogstore/entriesenumeratorandreturnerror_.md)
  Returns a log enumerator with default options for viewing the entries.
- [- entriesEnumeratorWithOptions:position:predicate:error:](./oslogstore/entriesenumeratorwithoptions_position_predicate_error_.md)
  Returns a log enumerator based on an underlying store.
### Initializers
- [init()](./oslogstore/init%28%29.md)
- [convenience init(scope: OSLogStore.Scope) throws](./oslogstore/init%28scope%29.md)
- [convenience init(URL: URL) throws](./oslogstore/init%28url%29-5nhb2.md)
### Enumerations
- [OSLogStore.Scope](./oslogstore/scope.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Read Log Entries
- [class OSLogEnumerator](./oslogenumerator.md)
  An enumerator that can access and list log entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore)*