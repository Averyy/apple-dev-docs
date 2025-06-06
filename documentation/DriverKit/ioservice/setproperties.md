# SetProperties

**Framework**: DriverKit  
**Kind**: method

Sends the dictionary of properties to the current service object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetProperties(OSDictionary * properties);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

The default implementation of this method returns [`kIOReturnUnsupported`](kioreturnunsupported.md). You can override this method and use it to modify the set of properties and values as needed. The changes you make apply only to the current service.

## Parameters

- `properties`: The registry properties to associate with the current service.

## See Also

- [CopyProperties](ioservice/copyproperties.md)
  Returns the registry properties associated with the current service.
- [SearchProperty](ioservice/searchproperty.md)
  Searches for a property with the specified name in the current service or one of its parent services, and returns the corresponding value.
- [IOPropertyName](iopropertyname.md)
  A string type for specifying the name of a property in the system’s registry.
- [IORegistryPlaneName](ioregistryplanename.md)
  A string type for specifying the name of a plane in the system’s registry.
- [Search Options](3325572-search_options.md)
  Options to apply when searching for registry properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/setproperties)*