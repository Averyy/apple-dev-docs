# publishedServiceRecord(with:)

**Framework**: IOBluetooth  
**Kind**: method

Adds a service to the local SDP server.

**Availability**:
- macOS ?+

## Declaration

```swift
class func publishedServiceRecord(with serviceDict: [AnyHashable : Any]!) -> Self!
```

#### Return Value

Returns an IOBluetoothSDPServiceRecord * with the attributes specified in the provided dictionary.

#### Discussion

Each entry in the dictionary representing the service contains the individual attributes. Each attribute in the dict is keyed by a string that must begin with a hex number representing the attribute ID. The key string may contain additional characters if desired as long as they follow a space after the ID hex string. The attribute value must follow the dictionary format described by IOBluetoothSDPDataElement. This dictionary format allows a service dict to be created as a plist file and then loaded into the system rather than built up in code. See the example code for an example of how can be done.

If the service record handle, L2CAP PSM or RFCOMM channel ID specified in the dictionary are in use, an alternate one will be assigned.

In addition to attributes that represent the service itself, additional attributes may be specified that control the local behavior of the service. To specify these local attributes, an additional property titled “LocalAttributes” may be added to the root of the service dict. The value of this property must be a dictionary that contains the individual local attributes.

Currently, only two local attributes are supported: “Persistent” and “TargetApplication”.

The “Persistent” local attribute must be either a boolean or number representing whether the service should be persistent. A persistent service will be saved off and restored any time the Bluetooth hardware is present. It will persist through reboots and can only be removed by calling IOBluetoothRemoveServiceWithRecordHandle(). This attribute is optional. By default, if no “Persistent” local property is present, the service will only exist temporarily. It will be removed either when IOBluetoothRemoveServiceWithRecordHandle() is called or when the client application exits.

The “TargetApplication” local attribute is used to specify an application to be launched when a remote device attempts to connect to the service (by opening either an L2CAP or RFCOMM channel of the type specified in the service). This value must be a string representing the absolute path to the target executable (not just the .app wrapper - i.e. /System/Library/CoreServices/OBEXAgent.app/Contents/MacOS/OBEXAgent). This attribute is optional. If no “TargetApplication” local attribute is specified, no special action will take place when an incoming connection to the service is created. It is up to the client to be monitoring for the connection and to do the right thing when one appears.

The “LocalAttributes” property is optional. If it is not specified, by default the created service is transient and will be removed when the client exits.

Additional local attributes to further control incoming services will be added in the future.

## Parameters

- `serviceDict`: A dictionary containing the attributes for the new service


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/publishedservicerecord(with:))*