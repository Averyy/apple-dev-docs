# PropertiesChanged

**Framework**: Core Audio  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
int (*)(const struct AudioServerPlugInHostInterface *, unsigned int, unsigned int, const struct AudioObjectPropertyAddress *) PropertiesChanged;
```

## Return Value

An OSStatus indicating success or failure.

## Discussion

This method informs the Host when the state of an plug-in’s object changes.

Note that for Device objects, this method is only used for state changes that don’t affect IO or the structure of the device.

## Parameters

- `inHost`: The AudioServerPlugInHostRef passed to the plug-in at initialization.
- `inObjectID`: The AudioObjectID of the object whose state has changed.
- `inNumberAddresses`: The number of elements in the inAddresses array.
- `inAddresses`: An array of AudioObjectPropertyAddresses for the changed properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostinterface/propertieschanged)*