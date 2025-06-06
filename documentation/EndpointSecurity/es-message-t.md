# es_message_t

**Framework**: Endpoint Security  
**Kind**: struct

A message from the Endpoint Security subsystem that describes a security event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_message_t
```

#### Overview

A message contains an [`event`](es_message_t/event.md) monitored by Endpoint Security and an [`action`](es_message_t/action.md) to perform. The [`event`](es_message_t/event.md) is a union of types specific to each kind of event. For example, a file-renaming event provides the source and destination paths as the union member `rename`. Similarly, a process fork event provides the process identifier of the new child process as the union member `fork`. Inspect the [`event_type`](es_message_t/event_type.md) to determine which member of the union to access.

A message can be an authorization request, or a notification of an event that has already taken place, as indicated by the [`action_type`](es_message_t/action_type.md) field. For authorization messages, your client handler calls [`es_respond_auth_result(_:_:_:_:)`](es_respond_auth_result(_:_:_:_:).md) or [`es_respond_flags_result(_:_:_:_:)`](es_respond_flags_result(_:_:_:_:).md) to authorize, deny, or pass behavior flags back to Endpoint Security.

## Topics

### Inspecting Message Properties
- [var action: es_message_t.__Unnamed_union_action](es_message_t/action.md)
  The action monitored by Endpoint Security.
- [var action_type: es_action_type_t](es_message_t/action_type.md)
  The type of action: authentication or notification.
- [struct es_action_type_t](es_action_type_t.md)
  The type of the message’s action.
- [struct es_event_id_t](es_event_id_t.md)
  An opaque identifier for events.
- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [var version: UInt32](es_message_t/version.md)
  The version of the Endpoint Security message.
### Identifying the Matched Event
- [var event: es_events_t](es_message_t/event.md)
  The event that triggered this message.
- [struct es_events_t](es_events_t.md)
  A C union of event-specific types.
- [var event_type: es_event_type_t](es_message_t/event_type.md)
  The type of the message’s event.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
### Inspecting Timing Properties
- [var time: timespec](es_message_t/time.md)
  The time the event occurred, expressed as a Darwin time value.
- [var mach_time: UInt64](es_message_t/mach_time.md)
  The time the event occurred, as a Mach time value.
- [var deadline: UInt64](es_message_t/deadline.md)
  The deadline by which your app must respond to the event.
- [var seq_num: UInt64](es_message_t/seq_num.md)
  The sequence number of the message.
- [var global_seq_num: UInt64](es_message_t/global_seq_num.md)
  The global sequence number of the message.
### Identifying the Source Process
- [var process: UnsafeMutablePointer<es_process_t>](es_message_t/process.md)
  The process that performed the action defined in a message.
- [struct es_process_t](es_process_t.md)
  A type that describes a process, as delivered by an Endpoint Security message.
### Inspecting Thread Properties
- [var thread: UnsafeMutablePointer<es_thread_t>?](es_message_t/thread.md)
  The thread that took the action defined in a message.
- [struct es_thread_t](es_thread_t.md)
  A structure that represents a thread in a process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t)*