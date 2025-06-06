# Message

**Framework**: Endpoint Security

A type used by Endpoint Security to notify your client when a monitored action occurs.

#### Overview

When Endpoint Security monitors an event of a given type, it sends a message to all clients subscribed to that event type, containing data about the event. Handlers use this information to react to the event. In the case of authorization events, handlers must actively respond to the message and authorize or deny the monitored action. The client must respond before the [`deadline`](es_message_t/deadline.md) specified by the message.

The following code shows a handler that reacts to events of the type [`ES_EVENT_TYPE_AUTH_RENAME`](es_event_type_auth_rename.md). Because the handler knows the event type, it can access the [`rename`](es_events_t/rename.md) member of the message’s [`event`](es_message_t/event.md) union. From this, it gets the [`source`](es_event_rename_t/source.md) of the rename event, and inspects the source file path. The handler denies authorization to the event if the filename includes the string `DONOTMOVE`, and allows it otherwise.

```c
es_handler_block_t handler = ^void  (es_client_t* _Nonnull client, const es_message_t* _Nonnull message) {
    switch (message->event_type) {
        case ES_EVENT_TYPE_AUTH_RENAME: {
            es_auth_result_t myResult = strstr(message->event.rename.source->path.data, "DONOTMOVE")
                ? ES_AUTH_RESULT_DENY : ES_AUTH_RESULT_ALLOW;
            es_respond_auth_result(client, message, myResult, false);
            break;
        }
        // Handle any other cases you have subscribed to with
        // additional case: statements.
        default:
            break;
    }
};

```

## Topics

### Inspecting Messages
- [struct es_message_t](es_message_t.md)
  A message from the Endpoint Security subsystem that describes a security event.
### Retaining and Releasing Messages
- [func es_retain_message(UnsafePointer<es_message_t>)](es_retain_message(_:).md)
  Retains the given message, extending its lifetime until released.
- [func es_release_message(UnsafePointer<es_message_t>)](es_release_message(_:).md)
  Releases a previously-retained message.
### Deprecated Functions
- [func es_copy_message(UnsafePointer<es_message_t>) -> UnsafeMutablePointer<es_message_t>?](es_copy_message(_:).md)
  Copies a message, by allocating new memory.
- [func es_message_size(UnsafePointer<es_message_t>) -> Int](es_message_size(_:).md)
  Calculates the size of a message structure.
- [func es_free_message(UnsafeMutablePointer<es_message_t>)](es_free_message(_:).md)
  Frees the memory allocated for the given message.
### Supporting Types
- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [struct es_string_token_t](es_string_token_t.md)
  A pointer to a null-terminated string, and the length in bytes of that string.
- [struct es_token_t](es_token_t.md)
  An arbitrary buffer of data with its size.

## See Also

- [Client](client.md)
  An opaque type that maintains Endpoint Security client state, and functions related to this type.
- [Event Types](event-types.md)
  Types used by messages to deliver details specific to different kinds of Endpoint Security events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/message)*