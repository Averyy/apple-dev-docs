# Turning an iOS device into an iBeacon device

**Framework**: Core Location

Broadcast iBeacon signals from an iOS device.

#### Overview

Any iOS device that supports sharing data using Bluetooth low energy can be turned into an iBeacon. Apps that use their underlying iOS device as an iBeacon must run in the foreground. As a result, use this feature for point-of-sale apps or for apps that are meant to run in the foreground anyway. For other types of iBeacon implementations, use dedicated beacon hardware from third-party manufacturers. To use an iOS device as an iBeacon, you do the following:

1. Obtain or generate a 128-bit UUID for your device.
2. Create a [`CLBeaconRegion`](clbeaconregion.md) object containing the UUID value along with appropriate major and minor values for your beacon.
3. Advertise the beacon information using the Core Bluetooth framework.

##### Get a Uuid for Your Device

The primary way to identify an iBeacon is from its UUID. When deploying one or more beacons, you assign a UUID to each one that conveys the beacon’s purpose to clients. The exact purpose of a beacon is something you define. For example, a department store chain might use the same UUID for all of its deployed beacons, or each store might be assigned a different UUID. Because detection involves using region monitoring to look for beacons with specific UUIDs, using fewer UUIDs is easier to manage.

To create a new UUID for your iBeacon deployment, use the `uuidgen` command-line tool. Open Terminal and type `uuidgen` on the command line and press Return. This tool generates a unique 128-bit value and formats it as an ASCII string that is punctuated by hyphens, as shown in Listing 1.

Listing 1. Generating a UUID from the command line

```shell
$ uuidgen
39ED98FF-2900-441A-802F-9C398FC199D2 
```

##### Configure the Beacon Region

Use a [`CLBeaconRegion`](clbeaconregion.md) object to configure your beacon’s identity. You use the beacon region to generate a dictionary of information that you can advertise later over Bluetooth. Listing 2 shows how to create a beacon region object and fill it with information.

Listing 2. Configuring your beacon’s identity

```swift
func createBeaconRegion() -> CLBeaconRegion? {
    let proximityUUID = UUID(uuidString:
                "39ED98FF-2900-441A-802F-9C398FC199D2")
    let major : CLBeaconMajorValue = 100
    let minor : CLBeaconMinorValue = 1
    let beaconID = "com.example.myDeviceRegion"
        
    return CLBeaconRegion(proximityUUID: proximityUUID!, 
                major: major, minor: minor, identifier: beaconID)
}
```

The UUID, major, and minor values are specific to your iBeacon implementation. You decide the meaning of these values and decide how apps that detect your beacons interpret those values.

##### Advertise Your Beacon Over Bluetooth

To broadcast your beacon’s identity from an iOS device, use the Core Bluetooth framework to configure the iOS device as a Bluetooth peripheral. When configured as a peripheral, your iOS device broadcasts its beacon information out to other devices using the Bluetooth hardware. Other devices use that information to perform ranging and detect their proximity to your iOS device.

Add the Core Bluetooth framework to your Xcode project. In your code, create a [`CBPeripheralManager`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheralManager) object and call its [`startAdvertising(_:)`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheralManager/startAdvertising(_:)) method to begin broadcasting your beacon data. The [`startAdvertising(_:)`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheralManager/startAdvertising(_:)) method takes a dictionary parameter that contains your beacon information. Call the [`peripheralData(withMeasuredPower:)`](clbeaconregion/peripheraldata(withmeasuredpower:).md) method of the [`CLBeaconRegion`](clbeaconregion.md) that you created previously to get a dictionary containing the data associated with your beacon.

Listing 3. Advertising your device over Bluetooth

```swift
func advertiseDevice(region : CLBeaconRegion) {
    let peripheral = CBPeripheralManager(delegate: self, queue: nil)
    let peripheralData = region.peripheralData(withMeasuredPower: nil)
        
    peripheral.startAdvertising(((peripheralData as NSDictionary) as! [String : Any]))
}
```

When calling the [`peripheralData(withMeasuredPower:)`](clbeaconregion/peripheraldata(withmeasuredpower:).md) method to obtain your data dictionary, you typically pass `nil` to specify the default received signal strength indicator (RSSI) value associated with the iOS device. This parameter represents the signal strength (in decibels) measured from one meter away from the device. You can specify custom values if you need to calibrate the device for better ranging performance in certain environments.

When you create a peripheral manager object, it calls the [`peripheralManagerDidUpdateState(_:)`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheralManagerDelegate/peripheralManagerDidUpdateState(_:)) method of its delegate object. You must implement this delegate method to ensure that Bluetooth low energy is supported and available to use on the iOS device.

> ❗ **Important**:  After advertising your app as a beacon, your app must continue running in the foreground to broadcast the needed Bluetooth signals. If the user quits the app, the system stops advertising the device as a peripheral over Bluetooth.

 After advertising your app as a beacon, your app must continue running in the foreground to broadcast the needed Bluetooth signals. If the user quits the app, the system stops advertising the device as a peripheral over Bluetooth.

During ranging, there may be a brief period in which Core Location creates two [`CLBeacon`](clbeacon.md) objects for the same iOS device. This behavior occurs because iOS changes the device’s Bluetooth identifier periodically to protect the user’s privacy, and one beacon represents the old identifier and one beacon represents the new identifier. Within 2 seconds of the identifier change, the beacon with the old identifier has its proximity property set to [`CLProximity.unknown`](clproximity/unknown.md). Within 10 seconds, the beacon with the old identifier is no longer reported.

## See Also

- [Ranging for Beacons](ranging-for-beacons.md)
  Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)
  Detect beacons and determine the relative distance to them.
- [class CLBeacon](clbeacon.md)
  Information about an observed iBeacon device and its relative distance to a person’s device.
- [protocol CLCondition](clcondition-swift.protocol.md)
  The abstract base class for all other monitor conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/turning-an-ios-device-into-an-ibeacon-device)*