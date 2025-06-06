# IOKitPersonalities

**Framework**: Bundle Resources  
**Kind**: dictionary

One or more groups of attributes that tell the system about the devices your driver supports.

**Availability**:
- macOS 10.0+

#### Discussion

This key contains a dictionary of driver , each of which specifies how to pair the driver to a device. Each key in the dictionary is a string you designate as the name of a specific personality, and the system doesn’t use your key names internally. The value of each key is a dictionary of attributes that describe the specific device to match with the driver. Thus, each key and dictionary combination represents a single personality of the driver. The system uses these personalities to match the driver to an attached device.

During the matching process, the system compares the attributes in each personality dictionary to data it obtained from the attached device. For example, if the personality dictionary includes the `VendorID` key, the system compares that key to the vendor information from the device. The system picks the driver that is compatible with the device and provides the best overall match. It then uses additional information from the personality dictionary to load and run the driver.

All personality dictionaries must include the following keys:

- [`CFBundleIdentifier`](information-property-list/cfbundleidentifier.md)
- [`IOProviderClass`](information-property-list/ioproviderclass.md)
- [`IOClass`](information-property-list/ioclass.md)

Include any of the following keys in your personality dictionary to customize the match criteria:

- [`IOPropertyMatch`](information-property-list/iopropertymatch.md)
- [`IONameMatch`](information-property-list/ionamematch.md)
- [`IOResourceMatch`](information-property-list/ioresourcematch.md)
- `IOParentMatch`
- `IOPathMatch`
- `IOMatchCategory`
- Device-specific keys, such as `DeviceUsagePairs`, `VendorID`, or `ProductID`. See a specific [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) subclass for information about the keys it supports.

Include one of more of the following keys to specify how to load your driver’s code:

- [`IOUserClass`](information-property-list/iouserclass.md)
- [`IOUserServerName`](information-property-list/iouserservername.md)
- [`IOUserClientClass`](information-property-list/iouserclientclass.md)

Use the following keys to further customize your driver’s behavior:

- `IOMatchDefer`. Set the value of this key to `true` to defer the matching process until after `kextd` starts.
- `IOUserServerOneProcess`. Set the value of this key to `true` to run your DriverKit services in one process. If the key is missing or its value is `false`, the system creates a separate process for each service.

## Topics

### Driver Classes
- [IOUserClass](information-property-list/iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOProviderClass](information-property-list/ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOClass](information-property-list/ioclass.md)
  The name of the class to instantiate from your driver.
- [IOUserClientClass](information-property-list/iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](information-property-list/iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.
### Advanced Match Criteria
- [IOPropertyMatch](information-property-list/iopropertymatch.md)
  The device-specific keys the system must match in order to use your driver.
- [IONameMatch](information-property-list/ionamematch.md)
  One or more strings that contain the names of possible provider objects in the system registry.
- [IOResourceMatch](information-property-list/ioresourcematch.md)
  One or more system-specific or device-specific resources that your driver requires.
- [IOParentMatch](information-property-list/ioparentmatch.md)
- [IOPathMatch](information-property-list/iopathmatch.md)
- [IOMatchCategory](information-property-list/iomatchcategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/iokitpersonalities)*