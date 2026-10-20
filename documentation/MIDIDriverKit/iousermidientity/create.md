# Create

**Framework**: MIDIDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit 24.0+

## Declaration

```c
static OSSharedPtr<IOUserMIDIEntity> Create(IOUserMIDIDriver *driver, IOUserMIDIDevice *device, OSString *name, IOUserMIDIProtocolID protocol, uint32_t numSources, uint32_t numDestinations);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mididriverkit/iousermidientity/create)*