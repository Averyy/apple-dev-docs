# dispatch_set_context

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Associates an application-defined context with the object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_set_context(dispatch_object_t object, void *context);
```

#### Discussion

Your application can associate custom context data with the object, to be used only by your application. Your application must allocate and deallocate the data as appropriate.

## Parameters

- `object`: This parameter cannot be `NULL`.
- `context`: The new application-defined context for the object. This can be `NULL`.

## See Also

### Updating Contextual Data
- [dispatch_get_context](./dispatch_get_context.md)
  Returns the application-defined context of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_set_context)*