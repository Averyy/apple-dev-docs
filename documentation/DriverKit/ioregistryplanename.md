# IORegistryPlaneName

**Framework**: DriverKit  
**Kind**: typealias

A string type for specifying the name of a plane in the system’s registry.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef char[128] IORegistryPlaneName;
```

## See Also

- [CopyProperties](ioservice/copyproperties.md)
  Returns the registry properties associated with the current service.
- [SetProperties](ioservice/setproperties.md)
  Sends the dictionary of properties to the current service object.
- [SearchProperty](ioservice/searchproperty.md)
  Searches for a property with the specified name in the current service or one of its parent services, and returns the corresponding value.
- [IOPropertyName](iopropertyname.md)
  A string type for specifying the name of a property in the system’s registry.
- [Search Options](3325572-search_options.md)
  Options to apply when searching for registry properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioregistryplanename)*