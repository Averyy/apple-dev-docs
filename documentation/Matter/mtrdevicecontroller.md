# MTRDeviceController

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRDeviceController
```

```objc
@interface MTRDeviceController : NSObject
```

## Mentions

- [Onboarding a Matter device](./onboarding-a-matter-device.md)

## Topics

### Initializers
- [init(parameters: MTRDeviceControllerAbstractParameters) throws](./mtrdevicecontroller/init%28parameters%29.md)
### Instance Properties
- [var controllerNodeID: NSNumber?](./mtrdevicecontroller/controllernodeid-6a04u.md)
- [var controllerNodeId: NSNumber?](./mtrdevicecontroller/controllernodeid-6a03y.md)
- [var isRunning: Bool](./mtrdevicecontroller/isrunning.md)
- [var uniqueIdentifier: UUID](./mtrdevicecontroller/uniqueidentifier.md)
- [var devices: [MTRDevice]](./mtrdevicecontroller/devices.md)
  Returns the list of MTRDevice instances that this controller has loaded into memory. Returns an empty array if no devices are in memory.
- [var isSuspended: Bool](./mtrdevicecontroller/issuspended.md)
  If true, the controller has been suspended via `suspend` and not resumed yet.
- [var nodesWithStoredData: [NSNumber]](./mtrdevicecontroller/nodeswithstoreddata.md)
  Returns the list of node IDs for which this controller has stored information.  Returns empty list if the controller does not have any information stored.
### Instance Methods
- [func add(MTRServerEndpoint) -> Bool](./mtrdevicecontroller/add%28_%29.md)
- [func attestationChallenge(forDeviceID: NSNumber) -> Data?](./mtrdevicecontroller/attestationchallenge%28fordeviceid%29.md)
- [func cancelCommissioning(forNodeID: NSNumber) throws](./mtrdevicecontroller/cancelcommissioning%28fornodeid%29.md)
- [func commissionDevice(UInt64, commissioningParams: MTRCommissioningParameters) throws](./mtrdevicecontroller/commissiondevice%28_,commissioningparams%29.md)
- [func commissionNode(withID: NSNumber, commissioningParams: MTRCommissioningParameters) throws](./mtrdevicecontroller/commissionnode%28withid,commissioningparams%29.md)
- [func computePaseVerifier(UInt32, iterations: UInt32, salt: Data) -> Data?](./mtrdevicecontroller/computepaseverifier%28_,iterations,salt%29.md)
- [func continueCommissioningDevice(UnsafeMutableRawPointer, ignoreAttestationFailure: Bool) throws](./mtrdevicecontroller/continuecommissioningdevice%28_,ignoreattestationfailure%29.md)
- [func deviceBeingCommissioned(withNodeID: NSNumber) throws -> MTRBaseDevice](./mtrdevicecontroller/devicebeingcommissioned%28withnodeid%29.md)
- [func fetchAttestationChallenge(forDeviceId: UInt64) -> Data?](./mtrdevicecontroller/fetchattestationchallenge%28fordeviceid%29.md)
- [func getBaseDevice(UInt64, queue: dispatch_queue_t, completionHandler: MTRDeviceConnectionCallback) -> Bool](./mtrdevicecontroller/getbasedevice%28_,queue,completionhandler%29.md)
- [func getDeviceBeingCommissioned(UInt64) throws -> MTRBaseDevice](./mtrdevicecontroller/getdevicebeingcommissioned%28_%29.md)
- [func openPairingWindow(UInt64, duration: Int) throws](./mtrdevicecontroller/openpairingwindow%28_,duration%29.md)
- [func openPairingWindow(withPIN: UInt64, duration: Int, discriminator: Int, setupPIN: Int) throws -> String](./mtrdevicecontroller/openpairingwindow%28withpin,duration,discriminator,setuppin%29.md)
- [func pairDevice(UInt64, address: String, port: UInt16, setupPINCode: UInt32) throws](./mtrdevicecontroller/pairdevice%28_,address,port,setuppincode%29.md)
- [func pairDevice(UInt64, discriminator: UInt16, setupPINCode: UInt32) throws](./mtrdevicecontroller/pairdevice%28_,discriminator,setuppincode%29.md)
- [func pairDevice(UInt64, onboardingPayload: String) throws](./mtrdevicecontroller/pairdevice%28_,onboardingpayload%29.md)
- [func preWarmCommissioningSession()](./mtrdevicecontroller/prewarmcommissioningsession%28%29.md)
- [func remove(MTRServerEndpoint, queue: dispatch_queue_t, completion: () -> Void)](./mtrdevicecontroller/remove%28_,queue,completion%29.md)
- [func setDeviceControllerDelegate(any MTRDeviceControllerDelegate, queue: dispatch_queue_t)](./mtrdevicecontroller/setdevicecontrollerdelegate%28_,queue%29.md)
- [func setNocChainIssuer(any MTRNOCChainIssuer, queue: dispatch_queue_t)](./mtrdevicecontroller/setnocchainissuer%28_,queue%29.md)
- [func setPairingDelegate(any MTRDevicePairingDelegate, queue: dispatch_queue_t)](./mtrdevicecontroller/setpairingdelegate%28_,queue%29.md)
- [func setupCommissioningSession(with: MTRSetupPayload, newNodeID: NSNumber) throws](./mtrdevicecontroller/setupcommissioningsession%28with,newnodeid%29.md)
- [func setupCommissioningSession(withDiscoveredDevice: MTRCommissionableBrowserResult, payload: MTRSetupPayload, newNodeID: NSNumber) throws](./mtrdevicecontroller/setupcommissioningsession%28withdiscovereddevice,payload,newnodeid%29.md)
- [func shutdown()](./mtrdevicecontroller/shutdown%28%29.md)
- [func startBrowse(forCommissionables: any MTRCommissionableBrowserDelegate, queue: dispatch_queue_t) -> Bool](./mtrdevicecontroller/startbrowse%28forcommissionables,queue%29.md)
- [func stopBrowseForCommissionables() -> Bool](./mtrdevicecontroller/stopbrowseforcommissionables%28%29.md)
- [func stopDevicePairing(UInt64) throws](./mtrdevicecontroller/stopdevicepairing%28_%29.md)
- [func add(any MTRDeviceControllerDelegate, queue: dispatch_queue_t)](./mtrdevicecontroller/add%28_,queue%29.md)
  Adds a Delegate to the device controller as well as the Queue on which the Delegate callbacks will be triggered
- [func forgetDevice(withNodeID: NSNumber)](./mtrdevicecontroller/forgetdevice%28withnodeid%29.md)
  Forget any information we have about the device with the given node ID.  That includes clearing any information we have stored about it.
- [func remove(MTRServerEndpoint)](./mtrdevicecontroller/remove%28_%29-2i5l5.md)
  Remove the given server endpoint without being notified when the removal completes.
- [func remove(any MTRDeviceControllerDelegate)](./mtrdevicecontroller/remove%28_%29-8pxve.md)
  Removes a Delegate from the device controller
- [func resume()](./mtrdevicecontroller/resume%28%29.md)
  Resume the controller.  This has no effect if the controller is not suspended.
- [func suspend()](./mtrdevicecontroller/suspend%28%29.md)
  Suspend the controller.  This will attempt to stop all network traffic associated with the controller.  The controller will remain suspended until it is resumed.
### Type Methods
- [class func computePASEVerifier(forSetupPasscode: NSNumber, iterations: NSNumber, salt: Data) throws -> Data](./mtrdevicecontroller/computepaseverifier%28forsetuppasscode,iterations,salt%29.md)
- [class func decodeXPCReadParams([String : Any]?) -> MTRReadParams?](./mtrdevicecontroller/decodexpcreadparams%28_%29.md)
- [class func decodeXPCResponseValues([[String : Any]]?) -> [[String : Any]]?](./mtrdevicecontroller/decodexpcresponsevalues%28_%29.md)
- [class func decodeXPCSubscribeParams([String : Any]?) -> MTRSubscribeParams?](./mtrdevicecontroller/decodexpcsubscribeparams%28_%29.md)
- [class func encodeXPCReadParams(MTRReadParams) -> [String : Any]?](./mtrdevicecontroller/encodexpcreadparams%28_%29.md)
- [class func encodeXPCResponseValues([[String : Any]]?) -> [[String : Any]]?](./mtrdevicecontroller/encodexpcresponsevalues%28_%29.md)
- [class func encodeXPCSubscribeParams(MTRSubscribeParams?) -> [String : Any]?](./mtrdevicecontroller/encodexpcsubscribeparams%28_%29.md)
- [class func sharedController(withID: (any NSCopying)?, xpcConnect: MTRXPCConnectBlock) -> MTRDeviceController](./mtrdevicecontroller/sharedcontroller%28withid,xpcconnect%29-5yhq4.md)
- [class func sharedController(withId: (any NSCopying)?, xpcConnect: MTRXPCConnectBlock) -> MTRDeviceController](./mtrdevicecontroller/sharedcontroller%28withid,xpcconnect%29-6rg64.md)
- [class func xpcInterfaceForClientProtocol() -> NSXPCInterface](./mtrdevicecontroller/xpcinterfaceforclientprotocol%28%29.md)
- [class func xpcInterfaceForServerProtocol() -> NSXPCInterface](./mtrdevicecontroller/xpcinterfaceforserverprotocol%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller)*