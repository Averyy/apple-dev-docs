---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct"
framework: "CareKit/CareKitStore"
---

# OCKRevisionRecord.KnowledgeVector

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

Knowledge vectors, also know as Lamport Timestamps, are used to determine the order of events in distributed systems that do not have a synchronized clock. If one knowledge vector is less than another, it means that the first event happened before the second. If one cannot be shown to be less than the other, it means the events are concurrent and require resolution.

## Declaration

```swift
struct KnowledgeVector
```

## Topics

### Operators
- [static func < (OCKRevisionRecord.KnowledgeVector, OCKRevisionRecord.KnowledgeVector) -> Bool](./knowledgevector-swift.struct/op%28_,_%29.md)
  A knowledge vector A is strictly less than another knowledge vector B if the clocks of all processes in A are less than or equal to those in B and at least one is strictly less than.
### Initializers
- [init([UUID : Int])](./knowledgevector-swift.struct/init%28_%29.md)
  Create a new `KnowledgeVector` in which only the entry for the current process is non-zero.
- [init(from: Decoder) throws](./knowledgevector-swift.struct/init%28from%29.md)
### Instance Properties
- [var processes: [UUID : Int]](./knowledgevector-swift.struct/processes.md)
  Each store involved in synchronization is termed a process and given a unique UUID. The corresponding integer for a process is an indication of time. If two processes have the same integer value, they both have the same knowledge of the current data representation.
- [var uuids: [UUID]](./knowledgevector-swift.struct/uuids.md)
  Returns all of the UUIDs registered in this vector.
### Instance Methods
- [func clock(for: UUID) -> Int](./knowledgevector-swift.struct/clock%28for%29.md)
  Returns the clock value for the current process.
- [func encode(to: Encoder) throws](./knowledgevector-swift.struct/encode%28to%29.md)
- [func increment(clockFor: UUID)](./knowledgevector-swift.struct/increment%28clockfor%29.md)
  Increment the vector entry for the current process.
- [func merge(with: KnowledgeVector)](./knowledgevector-swift.struct/merge%28with%29.md)
  Merge this vector with another.
### Default Implementations
- [Comparable Implementations](./knowledgevector-swift.struct/comparable-implementations.md)
- [Equatable Implementations](./knowledgevector-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Comparable
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct)*