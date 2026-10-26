# dispatch_get_context

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the application-defined context of an object.

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
extern void *dispatch_get_context(dispatch_object_t object);
```

#### Return Value

The context of the object; can be `NULL`.

#### Discussion

Your application can associate custom context data with the object, to be used only by your application. Your application must allocate and deallocate the data as appropriate.

## Parameters

- `object`: This parameter cannot be `NULL`.

## See Also

### Updating Contextual Data
- [dispatch_set_context](./dispatch_set_context.md)
  Associates an application-defined context with the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_get_context)*