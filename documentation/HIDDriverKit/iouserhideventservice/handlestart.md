# handleStart

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Performs additional initialization during the startup of the event service.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual bool handleStart(IOService *provider);
```

#### Return Value

`true` if initialization was successful, or `false` if an error occurred.

#### Discussion

The default implemention of this method does nothing.

## Parameters

- `provider`: The `IOService` provider for this object.

## See Also

### Running the Service
- [init](./init.md)
  Handles the basic initialization of the event service.
- [Start](./start.md)
  Starts the current event service and associates it with the specified provider object.
- [Stop](./stop.md)
  Stops the event service associated with the specified provider.
- [free](./free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/handlestart)*