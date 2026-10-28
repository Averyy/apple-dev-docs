---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents"
framework: "CareKit/CareKit"
---

# OCKTaskEvents

**Framework**: CareKit/CareKit  
**Kind**: struct  
**Role**: Structure

A data structure that holds events for multiple tasks.

## Declaration

```swift
struct OCKTaskEvents
```

## Overview

This data structure acts much like an ordered set. Events are ordered by least recently added, and an event is only valid if it is unique when compared to all other existing events. An event `x` is considered unique if:

1. The task associated with `x` has a non-nil stable identity.
2. There is no other event `y` in the data structure whose stable identity, and associated task’s stable identity, match that of `x`.

Stable identity is defined by the `id` property of the `Identifiable` protocol.

## Topics

### Initializers
- [init()](./ocktaskevents/init%28%29.md)
  Create an instance.
- [init(events: [OCKAnyEvent])](./ocktaskevents/init%28events%29.md)
  Create an instance.
### Instance Properties
- [var endIndex: Index](./ocktaskevents/endindex.md)
- [var id: String](./ocktaskevents/id.md)
- [var startIndex: Index](./ocktaskevents/startindex.md)
- [var tasks: [OCKAnyTask]](./ocktaskevents/tasks.md)
  Unique tasks.
### Instance Methods
- [func append(event: OCKAnyEvent) -> (OCKAnyEvent?, Bool)](./ocktaskevents/append%28event%29.md)
  Append an event. The event will only be appended if it unique.
- [func contains(event: OCKAnyEvent) -> Bool](./ocktaskevents/contains%28event%29.md)
- [func events(forTask: OCKAnyTask) -> [OCKAnyEvent]](./ocktaskevents/events%28fortask%29.md)
  Get all events that have matching tasks. Two tasks match if they have equal stable identities defined by the `Identifiable` protocol.
- [func index(after: Index) -> Index](./ocktaskevents/index%28after%29.md)
- [func makeIterator() -> Iterator](./ocktaskevents/makeiterator%28%29.md)
- [func remove(event: OCKAnyEvent) -> OCKAnyEvent?](./ocktaskevents/remove%28event%29.md)
- [func update(event: OCKAnyEvent) -> OCKAnyEvent?](./ocktaskevents/update%28event%29.md)
  Update an event with a particular uniqueness definition. The event will be inserted if it does not yet exist.
### Subscripts
- [subscript(Index) -> Iterator.Element](./ocktaskevents/subscript%28_%29-429hr.md)
- [subscript(Range<IndexPath.Index>) -> SubSequence](./ocktaskevents/subscript%28_%29-vzqu.md)
### Type Aliases
- [OCKTaskEvents.Element](./ocktaskevents/element.md)
- [OCKTaskEvents.Index](./ocktaskevents/index.md)
- [OCKTaskEvents.Iterator](./ocktaskevents/iterator.md)
- [OCKTaskEvents.SubSequence](./ocktaskevents/subsequence.md)
### Default Implementations
- [Collection Implementations](./ocktaskevents/collection-implementations.md)
- [Sequence Implementations](./ocktaskevents/sequence-implementations.md)

## Relationships

### Conforms To
- Swift.Collection
- Swift.Identifiable
- Swift.Sequence

## See Also

### Displaying care tasks in UIKit
- [class OCKTaskViewController](./ocktaskviewcontroller.md)
  A view controller that displays a task view and keeps it synchronized with a store.
- [class OCKSimpleTaskViewController](./ocksimpletaskviewcontroller.md)
  A view controller that display and updates a single event that can be completed or uncompleted by tapping a large button.
- [class OCKInstructionsTaskViewController](./ockinstructionstaskviewcontroller.md)
  A view controller that shows a detailed description for a single complete or incomplete event.
- [class OCKChecklistTaskViewController](./ockchecklisttaskviewcontroller.md)
  A view controller that shows detailed descriptions for complete or incomplete events, organized in a checklist.
- [class OCKGridTaskViewController](./ockgridtaskviewcontroller.md)
  A task view controller that displays multiple events in a grid collection view.
- [class OCKButtonLogTaskViewController](./ockbuttonlogtaskviewcontroller.md)
  A view controller that shows detailed descriptions for complete or incomplete events, organized in a grid.
- [class OCKSimpleTaskViewSynchronizer](./ocksimpletaskviewsynchronizer.md)
  A synchronizer for the simple task view.
- [class OCKInstructionsTaskViewSynchronizer](./ockinstructionstaskviewsynchronizer.md)
  A synchronizer for the instructions task view.
- [class OCKChecklistTaskViewSynchronizer](./ockchecklisttaskviewsynchronizer.md)
  A synchronizer for the checklist task view.
- [class OCKGridTaskViewSynchronizer](./ockgridtaskviewsynchronizer.md)
  A synchronizer that creates and updates a grid task view.
- [class OCKButtonLogTaskViewSynchronizer](./ockbuttonlogtaskviewsynchronizer.md)
  A synchronizer that creates and updates a button log task view.
- [protocol OCKTaskViewSynchronizerProtocol](./ocktaskviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for tasks.
- [protocol OCKAnyTaskViewSynchronizerProtocol](./ockanytaskviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for tasks.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents)*