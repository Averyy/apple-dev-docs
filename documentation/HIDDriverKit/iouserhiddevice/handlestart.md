# handleStart

**Framework**: HIDDriverKit  
**Kind**: method

Performs any custom initialization associated with starting the device service.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
bool handleStart(IOService * provider);
```

#### Return Value

`true` if initialization was successful, or `false` if it wasn’t.

#### Discussion

When defining a custom service, override this method and use it to perform any custom initialization. For example, you might allocate memory for your service’s instance variables and store a reference to the provider object for later use. The default implementation of this method returns `true`, and performs no other actions.

Don’t call this method yourself. The [`Start`](iouserhiddevice/start.md) method calls it when starting up the service.

## Parameters

- `provider`: The   provider for this object.

## See Also

- [Start](iouserhiddevice/start.md)
  Starts the device service and associates it with the specified provider object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhiddevice/handlestart)*