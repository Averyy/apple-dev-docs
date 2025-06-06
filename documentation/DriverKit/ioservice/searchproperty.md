# SearchProperty

**Framework**: DriverKit  
**Kind**: method

Searches for a property with the specified name in the current service or one of its parent services, and returns the corresponding value.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SearchProperty(const IOPropertyName name, const IORegistryPlaneName plane, uint64_t options, OSContainer * * property);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or [`kIOReturnNotFound`](kioreturnnotfound.md) if the property was not found.

#### Discussion

This method searches for the property in the current service first, followed by any parent services when applicable. The method returns the first instance of the property it finds.

## Parameters

- `name`: The name of the property as a c-string.
- `plane`: The name of the registry plane to search. The method uses this value only when you include   in the   parameter. If you don’t include that option, you may specify   for this parameter.
- `options`: Options to use during the search. Specify   to expand the search to include all parent services. If you don’t specify  , this method looks for the property only in the current service.
- `property`: If the specified property is found, this method puts the value in the provided variable; you are responsible for releasing that value. If the specified property isn’t found, this method sets the value of your variable to  .

## See Also

- [CopyProperties](ioservice/copyproperties.md)
  Returns the registry properties associated with the current service.
- [SetProperties](ioservice/setproperties.md)
  Sends the dictionary of properties to the current service object.
- [IOPropertyName](iopropertyname.md)
  A string type for specifying the name of a property in the system’s registry.
- [IORegistryPlaneName](ioregistryplanename.md)
  A string type for specifying the name of a plane in the system’s registry.
- [Search Options](3325572-search_options.md)
  Options to apply when searching for registry properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/searchproperty)*